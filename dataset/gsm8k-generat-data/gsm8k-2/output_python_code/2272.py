def solution():
    """Andrea buys herself a pony for her 30th birthday. She pays $500/month to rent a pasture for it, $10 a day for food, and $60/lesson for two lessons a week. How much does she spend on her pony in a year?"""
    pasture_rent_per_month = 500
    food_cost_per_day = 10
    lessons_per_week = 2
    lesson_cost = 60
    total_lessons_per_year = lessons_per_week * 52
    total_food_cost_per_year = food_cost_per_day * 365
    total_lesson_cost_per_year = lesson_cost * total_lessons_per_year
    total_pasture_rent_per_year = pasture_rent_per_month * 12
    total_cost = total_food_cost_per_year + total_lesson_cost_per_year + total_pasture_rent_per_year
    result = total_cost
    return result

print(solution())