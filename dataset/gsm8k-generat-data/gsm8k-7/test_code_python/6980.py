def solution():
    total_donuts = 50
    eaten_on_ride = 2
    eaten_by_secretary = 4
    half_eaten_during_meeting = 0.5

    # Calculate the number of remaining donuts
    remaining_donuts = total_donuts - eaten_on_ride - eaten_by_secretary
    remaining_donuts *= (1 - half_eaten_during_meeting)

    result = remaining_donuts
    return result

print(solution())