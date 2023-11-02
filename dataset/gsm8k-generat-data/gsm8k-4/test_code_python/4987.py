def solution():
    """A bottle of wine costs $20.00 today. When new tariffs are imposed in 2 months, the price of wine will increase by 25%. How much more expensive will 5 bottles of wine be in 2 months?"""
    # Define the initial price of a bottle of wine and the percentage increase
    initial_price = 20
    percentage_increase = 0.25

    # Calculate the new price of a bottle of wine after the tariff increase
    new_price = initial_price * (1 + percentage_increase)

    # Calculate the total cost of 5 bottles of wine at the new price
    total_cost_new = new_price * 5

    # Calculate the total cost of 5 bottles of wine at the initial price
    total_cost_initial = initial_price * 5

    # Calculate the difference in cost between the two scenarios
    cost_difference = total_cost_new - total_cost_initial
    
    result = cost_difference
    return result

print(solution())