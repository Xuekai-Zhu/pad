def solution():
    # Define the distances run each day
    monday_distance = 4.2
    tuesday_distance = 3.8
    wednesday_distance = 3.6
    thursday_distance = 4.4

    # Calculate the average distance
    average_distance = (monday_distance + tuesday_distance + wednesday_distance + thursday_distance) / 4
    result = average_distance
    return result

print(solution())