def solution():
    # Calculate the cost of one EpiPen after insurance coverage
    cost_per_epipen = 500 * (1 - 0.75) # insurance covers 75% of the cost

    # Calculate the total cost of EpiPens for a year
    cost_per_year = cost_per_epipen * 2 # John gets a new EpiPen every 6 months, so he gets 2 per year

    result = cost_per_year
    return result

print(solution())