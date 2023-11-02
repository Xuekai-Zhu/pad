def solution():
    monday_distance = 12
    tuesday_distance = 18
    wednesday_distance = 21

    # Calculate the total distance traveled over 3 days
    total_distance = monday_distance + tuesday_distance + wednesday_distance

    # Calculate the average distance traveled per day
    average_distance = total_distance / 3
    result = average_distance
    return result

print(solution())