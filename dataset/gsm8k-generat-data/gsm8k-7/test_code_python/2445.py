def solution():
    num_eyes = 0
    num_wrinkles = num_eyes * 3
    num_spots = num_wrinkles * 7

    # Calculate the total number of spots and wrinkles
    total_spots_wrinkles = num_wrinkles + num_spots

    # Calculate the difference between the number of eyes and the total spots/wrinkles
    diff_eyes_spots_wrinkles = total_spots_wrinkles - num_eyes

    result = diff_eyes_spots_wrinkles
    return result

print(solution())