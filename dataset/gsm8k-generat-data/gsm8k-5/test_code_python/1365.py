def solution():
    photos_stored = 400  # The computer drive already has 400 photos stored
    total_photos_space = 2000  # The computer drive has enough space to store 2000 photos
    photo_size = 1.5  # Each photo is 1.5 kilobytes in size
    video_size = 200  # Each video is 200 kilobytes in size

    # Calculate the remaining storage space after storing the photos
    remaining_space = total_photos_space - (photos_stored * photo_size)

    # Calculate the number of videos that can be stored
    videos_stored = remaining_space // video_size
    result = videos_stored
    return result

print(solution())