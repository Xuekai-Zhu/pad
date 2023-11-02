def solution():
    total_pictures = 30  # Louise hung a total of 30 pictures
    vertical_pictures = total_pictures // 2  # Half of the pictures are hung vertically
    haphazard_pictures = 5  # Louise hung the remaining 5 pictures haphazardly

    # Calculate the number of pictures hung horizontally
    horizontal_pictures = total_pictures - vertical_pictures - haphazard_pictures

    result = vertical_pictures
    return result

print(solution())