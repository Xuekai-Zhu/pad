def solution():
    initial_photos = 63
    deleted_bad_shots = 7
    cat_photos = 15
    photo_shoot = 0
    deleted_edited_photos = 3
    final_photos = 84

    # Calculate the total number of photos taken during the photo shoot
    photo_shoot = final_photos - (initial_photos - deleted_bad_shots + cat_photos + deleted_edited_photos)

    result = photo_shoot
    return result

print(solution())