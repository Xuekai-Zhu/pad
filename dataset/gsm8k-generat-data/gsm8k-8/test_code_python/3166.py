def solution():
    total_pictures = 30

    # Calculate the number of pictures hung horizontally
    horizontal_pictures = total_pictures / 2

    # Calculate the number of pictures hung haphazardly
    haphazard_pictures = 5

    # Calculate the number of pictures hung vertically
    vertical_pictures = total_pictures - horizontal_pictures - haphazard_pictures
    result = vertical_pictures
    return result

print(solution())