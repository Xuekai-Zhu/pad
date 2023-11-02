def solution():
    minutes_per_charge = 10  # The battery charge lasts 10 minutes
    minutes_per_room = 4  # It takes 4 minutes to vacuum each room
    total_rooms = 5  # Mary has 3 bedrooms, a kitchen, and a living room

    # Calculate the total time needed to vacuum the whole house
    total_time = total_rooms * minutes_per_room

    # Calculate the number of charges needed
    charges_needed = total_time // minutes_per_charge + 1  # Round up to the nearest whole number

    result = charges_needed
    return result

print(solution())