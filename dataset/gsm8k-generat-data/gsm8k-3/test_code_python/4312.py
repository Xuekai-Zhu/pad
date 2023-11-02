def solution():
    """Sean needs to replace 2 light bulbs in his bedroom, 1 in both the bathroom and the kitchen and 4 in the basement.  He also needs to replace 1/2 of that amount in the garage.  The bulbs come 2 per pack.  How many packs will he need?"""
    # Define the number of bulbs needed for each room
    bedroom_bulbs = 2
    bathroom_bulbs = 1
    kitchen_bulbs = 1
    basement_bulbs = 4
    garage_bulbs = (bedroom_bulbs + bathroom_bulbs + kitchen_bulbs + basement_bulbs) / 2

    # Calculate the total number of bulbs needed
    total_bulbs = bedroom_bulbs + bathroom_bulbs + kitchen_bulbs + basement_bulbs + garage_bulbs

    # Calculate the number of packs needed
    packs_needed = total_bulbs // 2

    result = packs_needed
    return result

print(solution())