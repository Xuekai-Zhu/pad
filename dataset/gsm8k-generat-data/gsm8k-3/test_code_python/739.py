def solution():
    """A vampire needs to suck 7 gallons of blood per week to survive. If he sucks 2 pints of blood per person, how many people does he need to suck each day to survive?"""
    # Define the amount of blood needed per week and per day
    WEEKLY_BLOOD = 7 * 128 # 1 gallon = 128 fluid ounces
    DAILY_BLOOD = WEEKLY_BLOOD / 7

    # Define the amount of blood sucked per person and convert it to fluid ounces
    BLOOD_PER_PERSON = 2 * 16 # 1 pint = 16 fluid ounces

    # Calculate the number of people the vampire needs to suck each day to survive
    people_per_day = DAILY_BLOOD / BLOOD_PER_PERSON

    # Display the result
    result = people_per_day
    return result

print(solution())