def solution():
    # Calculate total distance Mona biked for the week
    total_distance = 30 * 3

    # Subtract the distance biked on Wednesday and Saturday to get distance on Monday
    saturday_distance = 12 * 2
    monday_distance = (total_distance - 12 - saturday_distance) / 2
    result = monday_distance
    return result

print(solution())