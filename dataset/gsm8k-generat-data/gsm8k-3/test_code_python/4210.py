def solution():
    """For the gala luncheon planning committee, Margaret wants to serve chicken salad sandwiches using mini croissants.  She wants there to be enough food that each person on the committee can have 2 sandwiches each.  Her bakery offers 12 minis croissants for $8.00.  There are 24 people on the committee. How much will she spend on croissants?"""
    # Define the number of mini croissants in a pack and the cost of each pack
    CROISSANT_COUNT = 12
    CROISSANT_COST = 8.00

    # Calculate the total number of mini croissants needed
    croissant_count_needed = 24 * 2  # 2 sandwiches per person

    # Calculate the total number of packs of mini croissants needed
    packs_needed = croissant_count_needed / CROISSANT_COUNT
    if croissant_count_needed % CROISSANT_COUNT != 0:
        packs_needed += 1

    # Calculate the total cost of the mini croissants
    total_cost = packs_needed * CROISSANT_COST

    # Display the total cost
    result = total_cost
    return result

print(solution())