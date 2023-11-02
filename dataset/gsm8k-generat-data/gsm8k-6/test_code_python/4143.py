def solution():
    # Calculate the total number of passengers before cars cross the halfway point
    passengers_before_halfway = 20 * 3  # 20 cars with 2 passengers and 1 driver each

    # Calculate the total number of passengers after cars cross the halfway point
    passengers_after_halfway = 20 * 4  # 20 cars with 3 passengers and 1 driver each

    # Calculate the total number of passengers by the end of the race
    total_passengers = passengers_before_halfway + passengers_after_halfway

    result = total_passengers
    return result

print(solution())