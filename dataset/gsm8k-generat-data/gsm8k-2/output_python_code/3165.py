def solution():
    """Louise is hanging 30 of her pictures on the wall. She hangs some of them vertically, half of them horizontally, then hangs the remaining 5 pictures haphazardly. How many pictures did Louise hang vertically?"""
    total_pictures = 30
    horizontal_pictures = total_pictures / 2
    haphazard_pictures = 5
    vertical_pictures = total_pictures - horizontal_pictures - haphazard_pictures
    result = vertical_pictures
    return result

print(solution())