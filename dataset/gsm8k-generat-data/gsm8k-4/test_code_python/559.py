def solution():
    """Luna's monthly food budget is equal to 60% of her house rental budget while her phone bill budget is 10% of her food budget. If the total budget of house rental and food budget is $240, how much is Luna's total monthly budget to pay all those expenses?"""
    # Define the total budget for house rental and food
    total_budget = 240

    # Calculate the food budget as 60% of the house rental budget
    house_rental_budget = (total_budget / 1.6) * 0.6
    food_budget = total_budget - house_rental_budget

    # Calculate the phone bill budget as 10% of the food budget
    phone_bill_budget = food_budget * 0.1

    # Calculate the total monthly budget
    total_monthly_budget = total_budget + phone_bill_budget

    result = total_monthly_budget
    return result

print(solution())