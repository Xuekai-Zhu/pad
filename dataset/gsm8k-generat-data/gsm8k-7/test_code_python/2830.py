def solution():
    num_months = 12
    initial_savings = 2  # savings for January
    total_savings = initial_savings

    # Calculate the savings for each month and add it to the total savings
    for i in range(1, num_months):
        savings = initial_savings * (2 ** i)
        total_savings += savings

    result = total_savings
    return result

print(solution())