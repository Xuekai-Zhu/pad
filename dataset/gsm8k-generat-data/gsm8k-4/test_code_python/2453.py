def solution():
    """Toby has 63 photos on his camera roll. He deletes seven bad shots, takes fifteen pictures of his cat, and then does a photo shoot with his friends. After editing the photos with his friends, he decides to delete three of them. His camera roll has 84 photos in the end. How many photos did Toby take in the photo shoot?"""
    # Define the initial number of photos
    initial_photos = 63

    # Define the number of bad shots and the number of photos after they are deleted
    bad_shots = 7
    photos_after_bad_shots = initial_photos - bad_shots

    # Define the number of photos of Toby's cat and the number of photos after they are added
    cat_photos = 15
    photos_after_cat_photos = photos_after_bad_shots + cat_photos

    # Define the number of photos after the photo shoot and after editing
    edited_photos = 3
    final_photos = 84
    photos_after_photo_shoot = final_photos - edited_photos - photos_after_cat_photos

    # Return the result
    result = photos_after_photo_shoot
    return result

print(solution())