def solution():
    """Avery opens a flower shop. She ties 8 bunches of flowers with 9 flowers in each bunch. How many bunches would she have if she put 12 flowers in each bunch instead?"""
    
    # Determine the number of flowers in the original 8 bunches
    initial_flowers = 8 * 9
    
    # Determine the number of bunches with 12 flowers each
    new_bunches = initial_flowers // 12
    
    # Return the result
    result = new_bunches
    return result

print(solution())