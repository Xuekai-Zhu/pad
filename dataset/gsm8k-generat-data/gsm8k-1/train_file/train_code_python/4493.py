def solution():
    """Thomas started saving for a car almost 2 years ago. For the first year, his weekly allowance was $50. 
    In the second year, he got a job that pays $9 an hour at a coffee shop and worked 30 hours a week, 
    so his parents discontinued his allowance. 
    If the car he wants to buy is $15,000 and he spends $35 a week on himself, how much more money does Thomas need to buy the car by the end of the 2 years?"""
    
    first_year_allowance = 50 * 52
    second_year_wage = 9 * 30 * 52
    total_savings = first_year_allowance + second_year_wage
    total_spending = 35 * 104
    car_cost = 15000
    money_left = total_savings - total_spending
    money_needed = car_cost - money_left
    result = money_needed
    return result

print(solution())