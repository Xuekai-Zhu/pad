def solution():
    """Harrison buys a regular croissant on Saturdays for $3.50 and an almond croissant for $5.50 on Sundays. How much does he spend on croissants in a year?"""
    regular_croissant_price = 3.5
    almond_croissant_price = 5.5
    croissants_per_week = 2 # one regular and one almond croissant per week
    weeks_per_year = 52
    total_cost = croissants_per_week * (regular_croissant_price + almond_croissant_price) * weeks_per_year
    result = total_cost
    return result

print(solution())