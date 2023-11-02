def solution():
    """Jaynie wants to make leis for the graduation party. It will take 2 and half dozen plumeria flowers to make 1 lei. If she wants to make 4 leis, how many plumeria flowers must she pick from the trees in her yard?"""
    # Define the number of leis to be made
    leis_to_make = 4
    
    # Define the number of plumeria flowers needed for one lei
    flowers_per_lei = 2.5 * 12
    
    # Calculate the total number of plumeria flowers needed
    total_flowers_needed = leis_to_make * flowers_per_lei
    
    # Return the result
    result = total_flowers_needed
    return result

print(solution())