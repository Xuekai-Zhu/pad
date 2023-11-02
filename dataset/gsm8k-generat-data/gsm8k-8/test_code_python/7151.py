def solution():
    # Calculate the cost for one year of visiting once a month
    monthly_cost = 5 * 12
    yearly_cost = monthly_cost * 1

    # Calculate the cost for one year of visiting 4 times
    quarterly_cost = 7 * 4
    yearly_cost += quarterly_cost

    # Calculate the cost for 3 years of visiting
    total_cost = yearly_cost * 3
    result = total_cost
    return result

print(solution())