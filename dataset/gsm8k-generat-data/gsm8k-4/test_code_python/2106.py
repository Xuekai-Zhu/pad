def solution():
    """Together Felipe and Emilio needed a combined time of 7.5 years to build their homes. Felipe finished in half the time of Emilio. How many months did it take Felipe to build his house?"""
    # Define the combined time taken by Felipe and Emilio to build their homes
    total_time = 7.5

    # Let x be the time taken by Emilio to build his house
    # Then, Felipe took half the time, so he took x/2 time to build his house
    x = total_time * 2 / 3

    # Calculate the time taken by Felipe in months
    felipe_time = x / 2 * 12

    # return the result
    result = felipe_time
    return result

print(solution())