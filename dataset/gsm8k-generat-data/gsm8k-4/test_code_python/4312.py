def solution():
    """Sean needs to replace 2 light bulbs in his bedroom, 1 in both the bathroom and the kitchen and 4 in the basement.  He also needs to replace 1/2 of that amount in the garage.  The bulbs come 2 per pack.  How many packs will he need?"""
    # Define the number of light bulbs needed in each room
    bedroom_bulbs = 2
    bathroom_bulbs = 1
    kitchen_bulbs = 1
    basement_bulbs = 4

    # Calculate the total number of light bulbs needed
    total_bulbs = bedroom_bulbs + bathroom_bulbs + kitchen_bulbs + basement_bulbs
    total_bulbs += (total_bulbs / 2)  # Additional bulbs needed in the garage

    # Calculate the number of packs needed
    packs_needed = total_bulbs // 2

    result = packs_needed
    return result

print(solution())