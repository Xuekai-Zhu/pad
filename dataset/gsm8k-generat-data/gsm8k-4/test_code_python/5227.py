def solution():
    """Julian has 400 legos and wants to make lego models of two identical airplanes. If each airplane model requires 240 legos, how many more legos does Julian need?"""
    # Define the number of legos Julian has
    julian_legos = 400

    # Define the number of legos required to make one airplane model
    airplane_legos = 240

    # Calculate the total number of legos required to make two identical airplane models
    total_legos = airplane_legos * 2

    # Calculate the difference between the total required legos and the legos Julian has
    legos_needed = total_legos - julian_legos

    # return the result
    result = legos_needed
    return result

print(solution())