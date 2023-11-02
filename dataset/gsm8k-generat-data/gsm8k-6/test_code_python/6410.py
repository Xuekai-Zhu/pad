def solution():
    # Calculate the total cost for 5 lines at T-Mobile
    tmobile_cost = 50 + 50 + 16*3  # $50 for the first 2 lines and $16 for each additional line for 3 lines

    # Calculate the total cost for 5 lines at M-Mobile
    mmobile_cost = 45 + 45 + 14*3  # $45 for the first 2 lines and $14 for each additional line for 3 lines

    # Calculate the difference in cost between the two plans
    cost_difference = tmobile_cost - mmobile_cost
    result = cost_difference
    return result

print(solution())