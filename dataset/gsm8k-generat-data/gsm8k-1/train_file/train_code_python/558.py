def solution():
    """Luna's monthly food budget is equal to 60% of her house rental budget while her phone bill budget is 10% of her food budget. If the total budget of house rental and food budget is $240, how much is Luna's total monthly budget to pay all those expenses?"""
    total_budget = 240
    food_budget_percent = 60
    house_rental_budget_percent = 100 - food_budget_percent
    phone_bill_budget_percent = 10
    food_budget = total_budget * (food_budget_percent / 100)
    house_rental_budget = total_budget * (house_rental_budget_percent / 100)
    phone_bill_budget = food_budget * (phone_bill_budget_percent / 100)
    total_monthly_budget = total_budget + phone_bill_budget
    result = total_monthly_budget
    return result

print(solution())