def solution():
    """A portable computer drive has enough kilobytes of storage space to store 2000 photos. Each photo is 1.5 kilobytes in size. How many 200-kilobyte videos can it store if it already has 400 photos on it?"""
    # Define the total storage space in kilobytes
    total_storage = 2000 * 1.5

    # Calculate the remaining storage space after 400 photos are stored
    remaining_storage = total_storage - 400 * 1.5

    # Calculate the size of a 200-kilobyte video in kilobytes
    video_size = 200

    # Calculate the maximum number of 200-kilobyte videos that can be stored
    max_videos = remaining_storage // video_size

    # Return the result
    result = int(max_videos)
    return result

print(solution())