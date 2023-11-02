def solution():
    """Every month, Madeline has to buy food, treats, and medicine for her dog. Food costs $25 per week. Treats cost $20 per month. Medicine costs $100 per month. How much money does Madeline spend on her dog per year if there are 4 weeks in a month?"""
    weekly_food_cost = 25
    monthly_treat_cost = 20
    monthly_med_cost = 100
    yearly_cost = 12 * (4 * weekly_food_cost + monthly_treat_cost + monthly_med_cost)
    result = yearly_cost
    return result

print(solution())