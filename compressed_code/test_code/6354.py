def solution():
    
    gallons_per_week = 7
    gallons_per_day = gallons_per_week / 7
    pints_per_gallon = 8
    pints_per_person = 2
    people_per_day = (gallons_per_day * pints_per_gallon) / pints_per_person
    result = people_per_day
    return result

print(solution())