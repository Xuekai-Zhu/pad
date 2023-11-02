def solution():
    """A vampire needs to suck 7 gallons of blood per week to survive.  If he sucks 2 pints of blood per person, how many people does he need to suck each day to survive?"""
    # Define the amount of blood needed per week and per day
    WEEKLY_BLOOD_NEED = 7
    DAILY_BLOOD_NEED = WEEKLY_BLOOD_NEED / 7

    # Define the amount of blood sucked per person
    BLOOD_PER_PERSON = 2 / 8 

    # Calculate the number of people the vampire needs to suck each day
    people_needed = DAILY_BLOOD_NEED / BLOOD_PER_PERSON

    # Round up to the nearest whole number of people
    people_needed = int(people_needed) + 1

    result = people_needed
    return result

print(solution())