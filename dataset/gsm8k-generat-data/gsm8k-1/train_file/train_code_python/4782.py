def solution():
    """Ryan is considering buying a new multivitamin brand. Each pill has 50 mg of Vitamin A in it. The recommended daily serving of Vitamin A is 200 mg. How many pills does Ryan need to hit the recommended amount for the week?"""
    vitamin_per_pill = 50
    recommended_daily_vitamin = 200
    pills_per_day = recommended_daily_vitamin / vitamin_per_pill
    pills_per_week = pills_per_day * 7
    result = pills_per_week
    return result

print(solution())