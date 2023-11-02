def solution():
    """In a jar that has 50 ants, the number of ants in the jar doubles each hour. How many ants will be in the jar after 5 hours?"""
    # Define the initial number of ants in the jar
    initial_ants = 50

    # Calculate the number of ants after 5 hours
    ants_5_hours = initial_ants * (2 ** 5)

    # Display the total number of ants after 5 hours
    result = ants_5_hours
    return result

print(solution())