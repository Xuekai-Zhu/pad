def solution():
    num_people = 25
    water_per_person_per_day = 0.5
    distance_per_day = 200
    total_distance = 4000

    # Calculate the total number of gallons of water needed per day for all people
    total_water_per_day = num_people * water_per_person_per_day

    # Calculate the total number of days needed to travel the entire distance
    total_days = total_distance / distance_per_day

    # Calculate the total gallons of water needed for the entire journey
    total_water_needed = total_water_per_day * total_days
    result = total_water_needed
    return result

print(solution())