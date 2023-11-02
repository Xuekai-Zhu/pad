def solution():
    """Jill gets paid $20 per hour to teach and $30 to be a cheerleading coach. If she works 50 weeks a year, 35 hours a week as a teacher and 15 hours a week as a coach, what's her annual salary?"""
    teaching_rate = 20
    cheer_coaching_rate = 30
    teaching_hours_per_week = 35
    coaching_hours_per_week = 15
    weeks_per_year = 50
    
    teaching_pay_per_week = teaching_hours_per_week * teaching_rate
    coaching_pay_per_week = coaching_hours_per_week * cheer_coaching_rate
    annual_salary = (teaching_pay_per_week + coaching_pay_per_week) * weeks_per_year
    
    result = annual_salary
    return result

print(solution())