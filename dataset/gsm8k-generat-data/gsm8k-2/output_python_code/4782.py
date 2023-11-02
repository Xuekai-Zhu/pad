def solution():
    """Ryan is considering buying a new multivitamin brand. Each pill has 50 mg of Vitamin A in it. The recommended daily serving of Vitamin A is 200 mg. How many pills does Ryan need to hit the recommended amount for the week?"""
    daily_recommended = 200
    weekly_recommended = daily_recommended * 7
    pill_dose = 50
    pills_needed = weekly_recommended / pill_dose
    result = pills_needed
    return result

print(solution())