def solution():
    """Candice buys all the bread she and her family needs for the week from a local bakery. She needs 2 loaves of white bread for sandwiches that cost $3.50 each. She also needs a baguette that costs $1.50 and 2 loaves of sourdough bread that cost $4.50 each. She also treats herself to a $2.00 almond croissant each visit. How much does Candice spend at the bakery over 4 weeks?"""
    white_bread_cost = 3.5 * 2
    baguette_cost = 1.5
    sourdough_bread_cost = 4.5 * 2
    croissant_cost = 2
    total_cost_per_visit = white_bread_cost + baguette_cost + sourdough_bread_cost + croissant_cost
    total_cost_per_week = total_cost_per_visit * 1  # 1 time a week
    total_cost_per_4_weeks = total_cost_per_week * 4
    result = total_cost_per_4_weeks
    return result

print(solution())