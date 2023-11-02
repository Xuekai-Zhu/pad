def solution():
    # Find the remaining storage space after storing 400 photos
    remaining_space = 2000 - (400 * 1.5)

    # Calculate the number of 200-kilobyte videos that can be stored
    videos_stored = remaining_space // 200
    result = videos_stored
    return result

print(solution())