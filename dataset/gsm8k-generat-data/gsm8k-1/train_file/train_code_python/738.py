def solution():
    """A vampire needs to suck 7 gallons of blood per week to survive. If he sucks 2 pints of blood per person, how many people does he need to suck each day to survive?"""
    gallons_per_week = 7
    gallons_per_day = gallons_per_week / 7
    pints_per_gallon = 8
    pints_per_person = 2
    people_per_day = (gallons_per_day * pints_per_gallon) / pints_per_person
    result = people_per_day
    return result

print(solution())