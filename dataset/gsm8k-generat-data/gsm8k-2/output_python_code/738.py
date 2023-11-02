def solution():
    """A vampire needs to suck 7 gallons of blood per week to survive. If he sucks 2 pints of blood per person, how many people does he need to suck each day to survive?"""
    blood_per_week = 7*128 # converting gallons to pints
    blood_per_person = 2
    people_per_week = blood_per_week / blood_per_person
    people_per_day = people_per_week / 7
    result = round(people_per_day, 2)
    return result

print(solution())