def solution():
    # Define the initial and final cost per ticket
    initial_cost = 85
    final_cost = 102

    # Calculate the absolute increase
    increase = final_cost - initial_cost

    # Calculate the percent increase relative to the initial cost
    percent_increase = (increase / initial_cost) * 100

    result = percent_increase
    return result

print(solution())