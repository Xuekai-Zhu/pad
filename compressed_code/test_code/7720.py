def solution():
    
    num_eyes = 3
    num_wrinkles = num_eyes * 3
    num_spots = num_wrinkles * 7
    total_wrinkles_spots = num_wrinkles + num_spots
    eyes_difference = total_wrinkles_spots - num_eyes
    result = eyes_difference
    return result

print(solution())