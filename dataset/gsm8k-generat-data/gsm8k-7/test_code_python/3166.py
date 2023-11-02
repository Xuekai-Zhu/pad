def solution():
    total_pictures = 30
    horizontal_pictures = total_pictures / 2
    remaining_pictures = 5
    
    # Calculate the number of pictures hung vertically
    vertical_pictures = total_pictures - horizontal_pictures - remaining_pictures
    result = vertical_pictures
    return result

print(solution())