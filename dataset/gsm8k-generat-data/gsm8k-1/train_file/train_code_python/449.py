def solution():
    """Flora has been experiencing frequent fractures. Dr. Juan has asked her to strengthen her bones by drinking 105 gallons of milk within 3 weeks. Flora thinks that drinking 3 gallons of milk daily will be enough, but her brother says she'll still need to drink more. To fulfill Dr. Juan’s requirement, how many more gallons must Flora drink daily?"""
    total_gallons = 105
    weeks = 3
    gallons_per_week = total_gallons/weeks
    gallons_per_day = gallons_per_week/7
    current_gallon_per_day = 3
    additional_gallons = gallons_per_day - current_gallon_per_day
    result = additional_gallons
    return result

print(solution())