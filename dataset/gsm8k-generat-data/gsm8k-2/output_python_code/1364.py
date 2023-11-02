def solution():
    """A portable computer drive has enough kilobytes of storage space to store 2000 photos. Each photo is 1.5 kilobytes in size. How many 200-kilobyte videos can it store if it already has 400 photos on it?"""
    total_photo_storage = 2000 * 1.5
    remaining_storage = total_photo_storage - (400 * 1.5)
    video_size = 200
    videos = remaining_storage // video_size
    result = videos
    return result

print(solution())