def solution():
    # Define the production rate and number of days in each year
    production_rate = 10
    days_year1 = 365
    days_year2 = 365 * 0.9

    # Calculate the total production in each year
    production_year1 = production_rate * days_year1
    production_year2 = production_rate * days_year2

    # Calculate the total production in the second year after reducing by 10 percent
    production_year2 = production_year2 * 0.9
    result = production_year2
    return result

print(solution())