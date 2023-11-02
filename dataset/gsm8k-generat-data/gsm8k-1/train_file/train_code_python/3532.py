def solution():
    """The area of square A is 25. The area of square B is 81. What's the length difference between the sides of square A and B?"""
    area_A = 25
    area_B = 81
    side_length_A = round(area_A**0.5, 2)
    side_length_B = round(area_B**0.5, 2)
    length_difference = abs(side_length_B - side_length_A)
    result = length_difference
    return result

print(solution())