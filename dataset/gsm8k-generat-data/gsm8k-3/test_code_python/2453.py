def solution():
    """Toby has 63 photos on his camera roll. He deletes seven bad shots, takes fifteen pictures of his cat, and then does a photo shoot with his friends. After editing the photos with his friends, he decides to delete three of them. His camera roll has 84 photos in the end. How many photos did Toby take in the photo shoot?"""
    # Define the number of photos Toby started with
    initial_photos = 63

    # Define the number of photos deleted
    deleted_photos = 7 + 3

    # Define the number of photos of Toby's cat
    cat_photos = 15

    # Calculate the number of photos taken with Toby's friends
    friend_photos = 84 - initial_photos - deleted_photos - cat_photos

    # Display the number of photos taken with Toby's friends
    result = friend_photos
    return result

print(solution())