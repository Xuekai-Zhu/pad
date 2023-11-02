def solution():
    num_twenties = 10
    num_quarters = 140
    percent_spent = 3/5

    # Calculate the total value of all twenties
    total_twenties_value = num_twenties * 0.75

    # Calculate the total value of all quarters
    total_quarters_value = num_quarters * 0.75

    # Calculate the total value of all twenties
    total_twenties_value = num_twenties * 0.10

    # Calculate the total value of all quarters
    total_quarters_value = num_quarters * 0.25

    # Calculate the total amount paid for the lunch
    total_cost = total_twenties_value + total_quarters_value
    result = total_cost
    return result

print(solution())