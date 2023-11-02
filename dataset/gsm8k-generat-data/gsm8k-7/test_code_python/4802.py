def solution():
    battery_life = 10 # minutes
    time_per_room = 4 # minutes
    num_bedrooms = 3
    num_rooms_kitchen = 1
    num_rooms_living_room = 1
    total_rooms = num_bedrooms + num_rooms_kitchen + num_rooms_living_room

    # Calculate the total time needed to vacuum the whole house
    total_time = total_rooms * time_per_room

    # Calculate the number of times Mary needs to charge her vacuum cleaner
    num_charges_needed = total_time // battery_life + 1 # Round up to the nearest charge

    result = num_charges_needed
    return result

print(solution())