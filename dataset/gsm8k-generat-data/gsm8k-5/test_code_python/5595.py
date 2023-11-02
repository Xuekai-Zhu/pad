def solution():
    current_cost = 1000000  # The current cost of a ticket to Mars
    years_since_birth = 30  # Matty is 30 years old
    time_periods = years_since_birth / 10  # The number of times the cost has been halved

    # Calculate the new cost of a ticket to Mars
    new_cost = current_cost / (2 ** time_periods)
    result = new_cost
    return result

print(solution())