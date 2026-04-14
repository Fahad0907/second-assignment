def upload_avatar(user_id, image_file):
    filename = secure_filename(image_file.filename)
    image_file.save(f'uploads/{user_id}/{filename}')
    profile = UserProfile(user_id)
    profile.update_profile({'avatar': f'/uploads/{user_id}/{filename}'})
    return profile
