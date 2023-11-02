def solution():
    """A store received 20 pallets of paper products to stock. Half the pallets were paper towels,
    a quarter were tissues, and a fifth were paper plates. The rest were paper cups. How many pallets of paper cups did the store receive?"""
    
    # Calculate the number of pallets for each type of paper product
    towels_pallets = 20/2
    tissues_pallets = 20/4
    plates_pallets = 20/5
    
    # Calculate the total number of pallets for the types of paper products we know
    known_total_pallets = towels_pallets + tissues_pallets + plates_pallets
    
    # Calculate the number of pallets of paper cups
    cups_pallets = 20 - known_total_pallets
    
    # Display the number of pallets of paper cups
    result = cups_pallets
    return result

print(solution())