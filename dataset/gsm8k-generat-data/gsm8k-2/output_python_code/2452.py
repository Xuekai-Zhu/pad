def solution():
    """Toby has 63 photos on his camera roll. He deletes seven bad shots, takes fifteen pictures of his cat, and then does a photo shoot with his friends.
    After editing the photos with his friends, he decides to delete three of them. His camera roll has 84 photos in the end. How many photos did Toby take in the photo shoot?"""
    initial_photos = 63
    deleted_bad_shots = 7
    cat_photos = 15
    deleted_edited_shots = 3
    final_photos = 84
    photos_from_photo_shoot = final_photos - initial_photos + deleted_bad_shots - cat_photos + deleted_edited_shots
    result = photos_from_photo_shoot
    return result

print(solution())