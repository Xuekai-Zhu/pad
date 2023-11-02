def solution():
    
    num_eyes = 3
    num_wrinkles = num_eyes * 3
    num_spots = num_wrinkles * 7
    total_spots_wrinkles = num_spots + num_wrinkles
    difference = total_spots_wrinkles - num_eyes
    result = difference
    return result

print(solution())