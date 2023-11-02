def solution():
    initial_photos = 63  # Toby has 63 photos on his camera roll initially
    bad_shots = 7  # Toby deletes 7 bad shots
    cat_pictures = 15  # Toby takes 15 pictures of his cat
    edited_photos = 3  # Toby deletes 3 edited photos
    final_photos = 84  # Toby has 84 photos on his camera roll in the end

    # Calculate the number of photos taken during the photo shoot
    photo_shoot = final_photos - (initial_photos - bad_shots - cat_pictures - edited_photos)

    result = photo_shoot
    return result

print(solution())