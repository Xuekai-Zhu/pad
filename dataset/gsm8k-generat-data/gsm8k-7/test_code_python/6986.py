def solution():
    distance = 200
    cab_cost_per_mile = 2.5
    num_days = 7

    # Calculate the total distance that Briar will travel during the event (round-trip)
    total_distance = distance * 2

    # Calculate the total cost of all cab rides that Briar will take during the event
    total_cost = total_distance * cab_cost_per_mile * num_days
    result = total_cost
    return result

print(solution())