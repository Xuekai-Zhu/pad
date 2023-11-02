def solution():
    """In a jar that has 50 ants, the number of ants in the jar doubles each hour. How many ants will be in the jar after 5 hours?"""
    # Define the initial number of ants
    initial_ants = 50

    # Calculate the number of ants after 5 hours (doubling each hour)
    final_ants = initial_ants * (2 ** 5)

    # Return the result
    result = final_ants
    return result

print(solution())