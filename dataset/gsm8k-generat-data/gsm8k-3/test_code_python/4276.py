def solution():
    """It takes 320 rose petals to make an ounce of perfume. If each rose produces 8 petals, and there are 12 roses per bush, how many bushes will Fern have to harvest to make 20 12-ounce bottles of perfume?"""
    
    # Calculate the number of petals needed for each bottle of perfume
    petals_per_bottle = 320 * 12
    
    # Calculate the total number of petals needed for 20 bottles of perfume
    total_petals = petals_per_bottle * 20
    
    # Calculate the number of roses needed for the total number of petals
    roses_needed = total_petals / 8
    
    # Calculate the number of bushes needed
    bushes_needed = roses_needed / 12
    
    # Round up to the nearest whole number
    bushes_needed = math.ceil(bushes_needed)
    
    # Return the result
    result = bushes_needed
    return result

print(solution())