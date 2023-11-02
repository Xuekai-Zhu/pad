def solution():
    
    initial_photos = 63
    deleted_bad_shots = 7
    cat_photos = 15
    deleted_edited_shots = 3
    final_photos = 84
    photos_from_photo_shoot = final_photos - initial_photos + deleted_bad_shots - cat_photos + deleted_edited_shots
    result = photos_from_photo_shoot
    return result

print(solution())