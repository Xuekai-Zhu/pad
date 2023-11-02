def solution():
    num_people = 4
    total_hours = 16
    water_per_hour_per_person = 0.5

    # Calculate the total amount of water needed for all people for the whole trip
    total_water_needed = num_people * total_hours * water_per_hour_per_person

    # Round up to the nearest whole number of water bottles
    num_water_bottles = math.ceil(total_water_needed)

    result = num_water_bottles
    return result

print(solution())