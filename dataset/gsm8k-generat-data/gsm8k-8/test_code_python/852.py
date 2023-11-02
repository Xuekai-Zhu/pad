def solution():
    # Define the starting number of ants and the number of hours
    starting_ants = 50
    hours = 5

    # Calculate the number of ants after 5 hours
    ants_after_5_hours = starting_ants * 2**hours
    result = ants_after_5_hours
    return result

print(solution())