def solution():
    blood_per_week = 7  # The vampire needs to suck 7 gallons of blood per week
    blood_per_person = 2 / 8  # The vampire sucks 2 pints of blood, which is 1/8 of a gallon, per person
    people_per_day = (blood_per_week / blood_per_person) / 7  # Calculate the number of people the vampire needs to suck each day

    result = people_per_day
    return result

print(solution())