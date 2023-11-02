def solution():
    """Liezl prepared four sets of 2-dozen paper cups for her daughter's birthday party. If 5 cups were damaged and 30 were not used, how many paper cups were used?"""
    
    # Define the number of sets and dozens of paper cups
    num_sets = 4
    num_dozen = 2
    
    # Calculate the total number of paper cups prepared
    total_cups = num_sets * num_dozen * 12
    
    # Subtract the number of damaged and unused cups
    used_cups = total_cups - 5 - 30
    
    # Return the result
    result = used_cups
    return result

print(solution())