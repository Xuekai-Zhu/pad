def solution():
    """Flora has been experiencing frequent fractures. Dr. Juan has asked her to strengthen her bones by drinking 105 gallons of milk within 3 weeks. Flora thinks that drinking 3 gallons of milk daily will be enough, but her brother says she'll still need to drink more. To fulfill Dr. Juan’s requirement, how many more gallons must Flora drink daily?"""
    total_gallons = 105
    total_weeks = 3
    daily_gallons_goal = total_gallons / (total_weeks * 7)
    current_daily_gallons = 3
    additional_daily_gallons = daily_gallons_goal - current_daily_gallons
    result = additional_daily_gallons
    return result

print(solution())