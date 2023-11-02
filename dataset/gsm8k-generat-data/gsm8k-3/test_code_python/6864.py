def solution():
    """Liezl prepared four sets of 2-dozen paper cups for her daughter's birthday party. If 5 cups were damaged and 30 were not used, how many paper cups were used?"""
    # Define the number of sets and dozens of paper cups
    num_sets = 4
    dozens_per_set = 2

    # Calculate the total number of paper cups
    total_cups = num_sets * dozens_per_set * 12

    # Subtract the number of damaged and unused paper cups
    used_cups = total_cups - 5 - 30

    # Display the number of used paper cups
    result = used_cups
    return result

print(solution())