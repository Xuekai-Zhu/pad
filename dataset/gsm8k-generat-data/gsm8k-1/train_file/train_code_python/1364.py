def solution():
    """A portable computer drive has enough kilobytes of storage space to store 2000 photos. Each photo is 1.5 kilobytes in size. How many 200-kilobyte videos can it store if it already has 400 photos on it?"""
    storage_space = 2000 * 1.5
    space_used_by_photos = 400 * 1.5
    available_space = storage_space - space_used_by_photos
    video_size = 200
    videos_stored = available_space // video_size
    result = videos_stored
    return result

print(solution())