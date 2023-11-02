def solution():
    """Chantal knits sweaters to sell. Each sweater takes 4 balls of yarn. Each ball of yarn costs $6. How much money will Chantal gain in all 28 sweaters if she sells each sweater for $35?"""
    sweaters = 28
    yarn_balls_per_sweater = 4
    yarn_ball_cost = 6
    total_yarn_cost = sweaters * yarn_balls_per_sweater * yarn_ball_cost
    selling_price_per_sweater = 35
    total_earnings = sweaters * selling_price_per_sweater
    
    profit = total_earnings - total_yarn_cost
    result = profit
    return result

print(solution())