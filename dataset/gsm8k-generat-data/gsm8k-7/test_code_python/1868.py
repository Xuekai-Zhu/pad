def solution():
    total_distance = 5000
    initial_distance = 200
    alex_lead_1 = 300
    max_lead = 170
    alex_lead_2 = 440

    # Calculate the total distance covered by Alex
    alex_distance = initial_distance + alex_lead_1 + alex_lead_2

    # Calculate the distance left for Max to catch up to Alex
    distance_left = total_distance - initial_distance - alex_distance + max_lead
    result = distance_left
    return result

print(solution())