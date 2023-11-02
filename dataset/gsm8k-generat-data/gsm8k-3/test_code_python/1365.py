def solution():
    """A portable computer drive has enough kilobytes of storage space to store 2000 photos. Each photo is 1.5 kilobytes in size. How many 200-kilobyte videos can it store if it already has 400 photos on it?"""
    # Define the size of each photo and video in kilobytes
    PHOTO_SIZE = 1.5
    VIDEO_SIZE = 200

    # Define the maximum number of photos that can be stored on the drive
    MAX_PHOTOS = 2000

    # Calculate the remaining storage space in kilobytes
    remaining_space = (MAX_PHOTOS - 400) * PHOTO_SIZE

    # Calculate the number of 200-kilobyte videos that can be stored
    num_videos = remaining_space // VIDEO_SIZE

    # Display the result
    result = num_videos
    return result

print(solution())