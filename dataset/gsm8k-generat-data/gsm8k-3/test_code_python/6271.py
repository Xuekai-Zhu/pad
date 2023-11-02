def solution():
    """While on vacation in New York, Greg went out for a lunch that cost $100. If sales tax in New York is 4% and he left a 6% tip, how much did Greg pay?"""
    # Define the cost of the lunch
    lunch_cost = 100

    # Calculate the sales tax
    sales_tax = lunch_cost * 0.04

    # Calculate the tip
    tip = lunch_cost * 0.06

    # Calculate the total cost of the meal
    total_cost = lunch_cost + sales_tax + tip

    # Display the total cost
    result = total_cost
    return result

print(solution())