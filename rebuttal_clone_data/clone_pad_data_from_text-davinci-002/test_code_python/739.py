def solution():
    gallons_needed_per_week = 7
    pints_per_gallon = 8
    pints_needed_per_week = gallons_needed_per_week * pints_per_gallon
    pints_per_person = 2
    people_needed_per_day = pints_needed_per_week / pints_per_person / 7
    result = people_needed_per_day
    return result

print(solution())