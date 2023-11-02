def solution():
    """Since 1989, Lily has treated herself to 1 hydrangea plant, each year. Each plant costs $20.00. By 2021, how much money has Lily spent on hydrangeas?"""
    # Define the cost of each hydrangea plant and the start and end year
    HYDRANGEA_COST = 20
    START_YEAR = 1989
    END_YEAR = 2021

    # Calculate the number of years since 1989
    num_years = END_YEAR - START_YEAR + 1

    # Calculate the total cost of all the hydrangea plants
    total_cost = HYDRANGEA_COST * num_years

    # return the result
    result = total_cost
    return result

print(solution())