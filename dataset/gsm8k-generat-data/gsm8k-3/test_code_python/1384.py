def solution():
    """Bill is stocking the kitchenware section of the Walmart. He needs to stack 60 pots. On each shelf, he can stack five pots vertically and three sets of vertically stacked pots side-by-side. How many shelves does he need to stock all the pots?"""
    # Define the number of pots that can be stacked vertically and side-by-side
    POTS_VERTICAL = 5
    POTS_SIDE_BY_SIDE = 3

    # Define the total number of pots that need to be stocked
    total_pots = 60

    # Determine the number of sets of vertically stacked pots
    sets_of_stacked_pots = total_pots // (POTS_VERTICAL * POTS_SIDE_BY_SIDE)

    # If there are remaining pots, add another set of vertically stacked pots
    if total_pots % (POTS_VERTICAL * POTS_SIDE_BY_SIDE) != 0:
        sets_of_stacked_pots += 1

    # Determine the number of shelves needed to stock all the pots
    shelves_needed = sets_of_stacked_pots // 3

    # If there are remaining sets of stacked pots, add another shelf
    if sets_of_stacked_pots % 3 != 0:
        shelves_needed += 1

    # Display the number of shelves needed
    result = shelves_needed
    return result

print(solution())