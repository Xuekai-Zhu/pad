def solution():
    """Tom decides to renovate a house. There are 3 bedrooms and each bedroom takes 4 hours to renovate. The kitchen takes 50% longer than each bedroom. The living room took twice as much time as everything else combined. How long did everything take?"""
    # Define the time it takes to renovate each bedroom
    bedroom_time = 4

    # Calculate the time it takes to renovate the kitchen, which is 50% longer than a bedroom
    kitchen_time = bedroom_time * 1.5

    # Calculate the total time it takes to renovate the bedrooms and kitchen
    total_bed_kitchen_time = 3 * bedroom_time + kitchen_time

    # Calculate the time it takes to renovate the living room, which is twice as much as everything else combined
    living_room_time = total_bed_kitchen_time * 2

    # Calculate the total time it takes to renovate the entire house
    total_time = total_bed_kitchen_time + living_room_time

    result = total_time
    return result

print(solution())