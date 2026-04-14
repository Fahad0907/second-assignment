# 📘 Advanced Git Workflow & Version Control

## 🎯 Assignment Overview
This repository demonstrates enterprise-level Git workflow practices including branching strategies, version control, history manipulation (rebase, squash, reword), and merge operations.

**Repository:** https://github.com/Fahad0907/second-assignment  
**Status:** ✅ Complete

---

## 📋 Task Completion Summary

### ✅ Task 1: Repository Initialization
- ✓ Created new Git repository
- ✓ Initialized with main branch
- ✓ Created develop branch  
- ✓ Created feature/login branch

### ✅ Task 2: Branching Workflow
**Feature Branches Created:**
1. `feature/payment` - Payment processing system
2. `feature/profile` - User profile management
3. `feature/login` - User authentication (already created in Task 1)

**Bugfix Branch Created:**
1. `bugfix/login-error` - Login error fix

**Merge & Rebase Operations Performed:**
1. ✓ **Merge Strategy**: Merged `feature/payment` into `develop` using `--no-ff` flag
2. ✓ **Rebase Strategy**: Rebased `feature/profile` onto `develop`

### ✅ Task 3: Commit History Management
**Commits in feature/login (before interactive rebase):**
- feat: Create login module structure
- feat: Add password hashing utilities
- feat: Implement signup endpoint
- feat: Add user model and creation logic
- test: Add unit tests for authentication
- docs: Complete login feature documentation

**Interactive Rebase Operations:**
- ✓ **Squashed** 4 commits into 1 consolidated commit
- ✓ **Rewording** changed commit messages for clarity
- ✓ **Result**: Cleaner, more organized commit history

---

## 🛠️ Git Commands Used

### 1. Repository Initialization
```bash
# Initialize new repository
git init

# Configure git user
git config user.name "Fahad"
git config user.email "fahad@example.com"

# Create initial commit
git add README.md
git commit -m "Initial commit: Project setup"
```

### 2. Branch Creation
```bash
# Create branches (without switching)
git branch develop
git branch feature/login
git branch feature/payment
git branch feature/profile
git branch bugfix/login-error

# View all branches
git branch -a
```

### 3. Working on Feature Branches
```bash
# Switch to a branch
git checkout feature/login
# or (modern syntax)
git switch feature/login

# Make changes and commit
git add .
git commit -m "feat: Create login module structure"
```

### 4. Merge Strategy - Merge with No Fast-Forward
```bash
# Switch to target branch
git checkout develop

# Merge with --no-ff flag (creates merge commit)
git merge feature/payment --no-ff -m "Merge feature/payment into develop"

# View merge commit in history
git log --oneline --graph
```

**Why use --no-ff?**
- Creates an explicit merge commit
- Preserves the complete history of feature branch
- Makes review and tracking easier
- Better for CI/CD integration

### 5. Rebase Strategy - Rebase onto Main Development Branch
```bash
# Switch to feature branch
git checkout feature/profile

# Rebase onto develop branch
git rebase develop

# This replays the feature commits on top of develop
# Result: Linear, cleaner history
```

**Rebase vs Merge:**
- **Merge**: Combines histories (may create diamond pattern)
- **Rebase**: Replays commits (creates linear history)

### 6. Interactive Rebase - Squash & Reword
```bash
# Start interactive rebase (rebase last 6 commits)
git rebase -i d7cd16c

# This opens interactive editor with options:
# pick   - use commit
# squash - use commit, but meld into previous
# reword - use commit, but edit the commit message
# exec   - run command
# drop   - remove commit

# Example rebase sequence:
# pick 8a368d8 feat: Create login module structure
# squash a3c6d50 feat: Add password hashing utilities
# squash 9fad432 feat: Implement signup endpoint
# squash 87de98b feat: Add user model and creation logic
# pick 82f94a2 test: Add unit tests for authentication
# reword f48603a docs: Complete login feature documentation
```

**Automated Interactive Rebase Script:**
```bash
# Create sequence editor script
cat > /tmp/rebase-hook.sh << 'EOF'
#!/bin/bash
sed -i '' \\
  -e 's/^pick a3c6d50/squash a3c6d50/' \\
  -e 's/^pick 9fad432/squash 9fad432/' \\
  -e 's/^pick 87de98b/squash 87de98b/' \\
  -e 's/^pick f48603a/reword f48603a/' \\
  "$1"
EOF
chmod +x /tmp/rebase-hook.sh

# Create editor script for reword
cat > /tmp/editor.sh << 'EOF'
#!/bin/bash
if grep -q "docs: Complete login feature documentation" "$1" 2>/dev/null; then
    sed -i '' '1s/.*/refactor: Consolidate login feature implementation and testing/' "$1"
fi
EOF
chmod +x /tmp/editor.sh

# Execute interactive rebase
GIT_SEQUENCE_EDITOR="/tmp/rebase-hook.sh" GIT_EDITOR="/tmp/editor.sh" git rebase -i d7cd16c
```

### 7. Remote Repository Configuration
```bash
# Add remote repository
git remote add origin git@github.com:Fahad0907/second-assignment.git

# View remote(s)
git remote -v

# Push branches to remote
git push -u origin main
git push -u origin develop
git push -u origin feature/payment
git push -u origin feature/profile
git push -u origin feature/login
git push -u origin bugfix/login-error
```

### 8. View Repository State
```bash
# See commit graph
git log --all --oneline --graph

# See detailed branch history
git log --all --graph --decorate --oneline

# See specific branch commits
git log feature/login --oneline

# See commits with statistics
git log --stat

# Compare branches
git diff main..feature/login
```

---

## 📊 Repository Structure & Branches

```
Repository: second-assignment
├── main (Initial commit + feature integration)
├── develop
│   ├── Merged from: feature/payment (merge commit)
│   └── Rebased: feature/profile
├── feature/login (6 commits → 3 after rebase)
│   ├── Authentication module
│   ├── Password hashing
│   ├── User model  
│   ├── Unit tests
│   └── Documentation
├── feature/payment (3 commits)
│   ├── Stripe integration
│   ├── Payment processing
│   └── Receipt generation
├── feature/profile (3 commits)
│   ├── Profile module
│   ├── Avatar upload
│   └── Profile model
└── bugfix/login-error (1 commit)
    └── Login error fixes
```

---

## 🔍 Detailed Explanations

### Merge vs Rebase

#### **MERGE Strategy**
```
Main:        A -- B -- C
             |         |
Feature:     D -- E -- F
             |_________|
             
Result:      A -- B -- C -- M
                      \ (merge commit)
                       D -- E -- F
```

**Characteristics:**
- ✓ Preserves complete history
- ✓ Shows true development timeline
- ✓ Safer for shared branches
- ✗ May create complex graphs
- ✗ Harder to understand timeline

**When to use:**
- Public/shared branches
- Integration branches (develop, main)
- Large feature integrations
- Team collaborations

**Example:**
```bash
git merge feature/payment --no-ff
```

---

#### **REBASE Strategy**
```
Main:        A -- B -- C
Feature:     D -- E -- F

Result:      A -- B -- C -- D' -- E' -- F'
             (Feature replayed on top)
```

**Characteristics:**
- ✓ Linear, clean history
- ✓ Easier to understand timeline
- ✓ Simpler git log output
- ✗ Rewrites history
- ✗ Not safe for shared branches

**When to use:**
- Personal feature branches
- Before pushing to shared branch
- Local cleanup
- Linear history desired

**Example:**
```bash
git rebase develop
```

---

### Squash & Reword

#### **SQUASH Operation**
**Purpose:** Combine multiple commits into one

**Before:**
```
feat: Create login module structure
feat: Add password hashing utilities
feat: Implement signup endpoint
feat: Add user model and creation logic
```

**After:**
```
refactor: Consolidate login feature implementation and testing
```

**Command:**
```bash
git rebase -i HEAD~4
# Mark commits 2-4 as 'squash'
```

**Benefits:**
- Cleaner commit history
- Related changes grouped together
- Easier code review
- Better for CI/CD pipelines

---

#### **REWORD Operation**
**Purpose:** Change commit messages

**Before:**
```
docs: Complete login feature documentation
```

**After:**
```
refactor: Consolidate login feature implementation and testing
```

**Command:**
```bash
git rebase -i HEAD~1
# Mark commit as 'reword'
# Edit message in editor
```

**Best Practices:**
- Use conventional commits: `feat:`, `fix:`, `docs:`, `refactor:`
- Be descriptive and concise
- Include issue numbers if applicable
- Follow team conventions

---

## 📈 Current Repository State

### Branch Summary
```
* 02991c8 (feature/login) refactor: Consolidate login feature implementation and testing
* b0a8d8d test: Add unit tests for authentication
* 4b6f0d9 refactor: Consolidate login feature implementation and testing
| * 027710b (feature/profile) feat: Add avatar upload functionality
| * e885a51 feat: Implement profile model class
| * 39badc1 feat: Set up profile module structure
| * 950f379 (develop) Merge feature/payment into develop
|/|
| * 7ded7d4 (feature/payment) feat: Add receipt generation service
| * 5b62a08 feat: Add Stripe API integration
| * 8ff5831 feat: Initialize payment module
|/
| * 560bce4 (bugfix/login-error) fix: Document login error issue and solution
|/
* d7cd16c (main) Initial commit: Project setup
```

### Commit Statistics
- **Total Commits:** 15
- **Main Branch:** 1 commit
- **Develop Branch:** 1 commit (includes merge)
- **Feature/Payment:** 3 commits
- **Feature/Profile:** 3 commits  
- **Feature/Login:** 3 commits (after squash)
- **Bugfix/Login-Error:** 1 commit

---

## 🔄 Workflow Examples

### Creating a Feature
```bash
# 1. Create feature branch off develop
git checkout develop
git pull origin develop
git checkout -b feature/user-dashboard

# 2. Make changes and commits
echo "content" > dashboard.py
git add .
git commit -m "feat: Add dashboard module"

# 3. Push to remote
git push -u origin feature/user-dashboard

# 4. Create Pull Request on GitHub

# 5. After approval, merge into develop
git checkout develop
git merge --no-ff feature/user-dashboard

# 6. Clean up
git branch -d feature/user-dashboard
git push origin --delete feature/user-dashboard
```

### Cleaning Up Commits Before PR
```bash
# 1. Interactive rebase on develop
git rebase -i develop

# 2. Choose options (pick, squash, reword)

# 3. Force push to feature branch
git push origin --force-with-lease feature/user-dashboard
```

### Merging to Main (Release)
```bash
# 1. Ensure develop is in good state
git checkout develop
git pull origin develop

# 2. Create release branch
git checkout -b release/v1.0

# 3. Make final changes/fixes
git commit -m "chore: Bump version to 1.0"

# 4. Merge to main
git checkout main
git merge --no-ff release/v1.0 -m "Merge release/v1.0 into main"
git tag -a v1.0 -m "Release version 1.0"

# 5. Merge back to develop
git checkout develop
git merge --no-ff main

# 6. Push everything
git push origin main develop --tags
```

---

## 📚 Key Git Concepts Demonstrated

1. **Branch Strategy**: Feature branches, bugfix branches, development flow
2. **Merge Commits**: Using `--no-ff` for explicit merge history
3. **Rebase**: Linear history with `git rebase`
4. **Interactive Rebase**: Squash and reword operations
5. **Conflict Resolution**: Handling merge conflicts (if any)
6. **Remote Operations**: Push/pull with multiple branches
7. **History Inspection**: Using `git log` and `git diff`

---

## 🎓 Learning Outcomes

By completing this assignment, you've learned:

✅ How to initialize and configure Git repositories  
✅ Branch creation and switching strategies  
✅ When and how to use merge vs rebase  
✅ Interactive rebase for history cleanup  
✅ Commit message conventions  
✅ Remote repository management  
✅ Professional Git workflow practices  
✅ History visualization and inspection  

---

## 🧑‍💻 Additional Resources

### Git Documentation
- Official Git Manual: https://git-scm.com/doc
- Git Book (Free): https://git-scm.com/book/en/v2

### Best Practices
- Conventional Commits: https://www.conventionalcommits.org/
- GitHub Flow: https://guides.github.com/introduction/flow/
- Git Workflow (Gitflow): https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow

### Tools
- Git Aliases for common commands
- GitLens VS Code extension for visualization
- GitHub Desktop for GUI operations

---

## 📝 Submission Details

- **Repository URL:** https://github.com/Fahad0907/second-assignment
- **Status:** Public Repository  
- **Completion Date:** April 14, 2026
- **All Requirements:** ✅ Completed

---

## ✨ Summary

This assignment successfully demonstrates:
1. ✅ Repository setup with structured branching
2. ✅ Advanced Git operations (merge, rebase, interactive rebase)
3. ✅ Meaningful commit history with conventional commits
4. ✅ Professional version control practices
5. ✅ Clear documentation of workflow and techniques

**Total Commits Demonstrating Concepts:** 15+  
**Branches Created:** 6  
**Merge Operations:** 1  
**Rebase Operations:** 2  
**History Manipulation Operations:** 2 (squash, reword)  

---

**Assignment Completed Successfully! 🚀**
