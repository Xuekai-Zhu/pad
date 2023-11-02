def solution():
    initial_photos = 63
    deleted_bad_shots = 7
    cat_photos = 15
    photos_with_friends = 84 - initial_photos - deleted_bad_shots - cat_photos - 3

    result = photos_with_friends
    return result

print(solution())