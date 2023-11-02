def solution():
    monday_distance = 4.2
    tuesday_distance = 3.8
    wednesday_distance = 3.6
    thursday_distance = 4.4

    # Calculate the total distance Terese runs during the week
    total_distance = monday_distance + tuesday_distance + wednesday_distance + thursday_distance

    # Calculate the average distance Terese runs each day
    average_distance = total_distance / 4
    result = average_distance
    return result

print(solution())