def solution():
    
    total_pictures = 30
    horizontal_pictures = total_pictures / 2
    haphazard_pictures = 5
    vertical_pictures = total_pictures - horizontal_pictures - haphazard_pictures
    result = vertical_pictures
    return result

print(solution())