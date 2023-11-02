def solution():
    total_pictures = 72
    num_albums = 8
    num_selfies = 3
    num_portraits = 2

    # Calculate the number of pics in each album
    pics_per_album = total_pictures / num_albums

    # Calculate the number of portraits in each album
    portraits_per_album = pics_per_album - num_selfies - num_portraits

    result = portraits_per_album
    return result

print(solution())