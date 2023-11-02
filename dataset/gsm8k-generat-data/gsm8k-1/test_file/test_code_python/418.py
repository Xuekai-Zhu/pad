Unfortunately, as an AI language model, I cannot provide a solution to the Samantha's last name problem as it requires more information or context. As for the streaming service problem, we need to calculate the total cost of the service for 2 years, taking into account the introductory deal and the increase in price. Here's the solution:

def solution():
    """Bill is signing up for a new streaming service. He got a special introductory deal where the first 6 months were $8 a month, then it went up to the normal price of $12 a month. After 8 months of the normal rate, the service increased its price to $14 a month. How much do 2 years of the service cost him?"""
    months_per_year = 12
    introductory_months = 6
    introductory_price = 8
    normal_price = 12
    increased_price = 14
    
    # total cost for first 6 months
    cost_introductory = introductory_months * introductory_price
    
    # total cost for 8 months of normal price
    cost_normal_8_months = 8 * normal_price
    
    # total cost for remaining months at increased price
    cost_increased_price = (24 - introductory_months - 8) * increased_price
    
    # total cost for 2 years
    total_cost = cost_introductory + cost_normal_8_months + cost_increased_price
    
    result = total_cost
    
    return result

print(solution())