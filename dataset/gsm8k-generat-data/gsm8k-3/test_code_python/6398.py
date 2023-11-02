def solution():
    """Since 1989, Lily has treated herself to 1 hydrangea plant, each year. Each plant costs $20.00. By 2021, how much money has Lily spent on hydrangeas?"""
    # Define the cost of each hydrangea plant
    HYDRANGEA_COST = 20.0

    # Calculate the number of years since 1989
    years = 2021 - 1989

    # Calculate the total cost of all the hydrangea plants
    total_cost = years * HYDRANGEA_COST

    # Display the total cost
    result = total_cost
    return result

print(solution())