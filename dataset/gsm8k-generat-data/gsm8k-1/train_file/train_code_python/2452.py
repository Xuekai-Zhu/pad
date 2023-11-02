def solution():
    """Toby has 63 photos on his camera roll. He deletes seven bad shots, takes fifteen pictures of his cat, and then does a photo shoot with his friends. After editing the photos with his friends, he decides to delete three of them. His camera roll has 84 photos in the end. How many photos did Toby take in the photo shoot?"""
    initial_photos = 63
    deleted_photos = 7 + 3
    cat_photos = 15
    end_photos = 84
    shoot_photos = end_photos - initial_photos - deleted_photos - cat_photos
    result = shoot_photos
    
    return result

print(solution())