def solution():
    initial_ants = 50  # Starting with 50 ants
    hours = 5  # After 5 hours

    # Calculate the total number of ants after 5 hours
    total_ants = initial_ants * (2 ** hours)
    result = total_ants
    return result

print(solution())