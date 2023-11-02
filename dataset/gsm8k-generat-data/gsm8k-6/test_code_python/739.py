def solution():
    # Calculate the amount of blood the vampire needs to suck per day
    gallons_per_day = 7 / 7  # 7 gallons of blood per week, divided by 7 days in a week
    pints_per_day = gallons_per_day * 8  # 1 gallon = 8 pints
    # Calculate the number of people he needs to suck every day
    people_per_day = pints_per_day / 2  # 2 pints of blood per person
    result = people_per_day
    return result

print(solution())