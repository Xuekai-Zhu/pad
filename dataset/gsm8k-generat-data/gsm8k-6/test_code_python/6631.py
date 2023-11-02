def solution():
    # Calculate the number of people who receive the stimulus
    num_people_stimulus = 1000 * 0.2

    # Calculate the cost of the stimulus
    cost_stimulus = num_people_stimulus * 2000

    # Calculate the amount of tax revenue generated from the stimulus
    tax_revenue = cost_stimulus * 5

    # Calculate the profit (tax revenue - cost)
    profit = tax_revenue - cost_stimulus
    result = profit
    return result

print(solution())