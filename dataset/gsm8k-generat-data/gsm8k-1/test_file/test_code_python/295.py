def solution():
    """John hires a driving service to get him to work each day. His work is 30 miles away and he has to go there and back each day. He goes to work 5 days a week for 50 weeks a year. He gets charged $2 per mile driven and he also gives his driver a $150 bonus per month. How much does he pay a year for driving?"""
    miles_per_day = 60
    days_per_week = 5
    weeks_per_year = 50
    cost_per_mile = 2
    driver_bonus = 150 * 12
    total_miles = miles_per_day * days_per_week * weeks_per_year
    cost_per_year = total_miles * cost_per_mile + driver_bonus
    result = cost_per_year
    return result

print(solution())