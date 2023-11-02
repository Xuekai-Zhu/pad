def solution():
    """Samuel is going to the cinema with his brother, Kevin. They both have a total budget of $20 for their outing. Samuel buys his $14 ticket, then spends $6 on drinks and food. Kevin buys his ticket, then spends $2 on drinks. They have both used their entire budget. How much did Kevin spend on food?"""
    total_budget = 20
    samuel_ticket = 14
    samuel_food_drinks = 6
    kevin_ticket = total_budget - samuel_ticket
    kevin_food = total_budget - samuel_ticket - samuel_food_drinks - kevin_ticket
    result = kevin_food
    return result

print(solution())