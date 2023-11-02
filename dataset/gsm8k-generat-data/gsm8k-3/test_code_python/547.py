def solution():
    """ Tom decides to renovate a house. There are 3 bedrooms and each bedroom takes 4 hours to renovate. The kitchen takes 50% longer than each bedroom. The living room took twice as much time as everything else combined. How long did everything take? """
    # Define the number of bedrooms and the time it takes to renovate each bedroom
    num_bedrooms = 3
    bedroom_time = 4

    # Calculate the total time to renovate all the bedrooms
    bedroom_total_time = num_bedrooms * bedroom_time

    # Calculate the time it takes to renovate the kitchen
    kitchen_time = bedroom_time * 1.5

    # Calculate the time it takes to renovate the living room
    living_room_time = (bedroom_total_time + kitchen_time) * 2

    # Calculate the total time for the entire renovation
    total_time = bedroom_total_time + kitchen_time + living_room_time

    # Display the total time
    result = total_time
    return result

print(solution())