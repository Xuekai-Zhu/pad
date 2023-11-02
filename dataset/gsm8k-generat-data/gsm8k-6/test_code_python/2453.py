def solution():
    # Calculate the number of photos Toby took in the photo shoot
    initial_photos = 63  # initial number of photos
    deleted_bad_shots = 7  # number of bad shots deleted
    cat_photos = 15  # number of cat photos added
    edited_photos = 3  # number of photos deleted after editing
    remaining_photos = 84  # total number of photos at the end
    photo_shoot_photos = remaining_photos - initial_photos + deleted_bad_shots - cat_photos - edited_photos  # number of photos taken in the photo shoot
    result = photo_shoot_photos
    return result

print(solution())