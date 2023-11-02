def solution():
    """Tom invites his parents and 3 siblings to his house. They each eat 3 times a day. How many plates do Tom and his guests use while they are there for the 4 days if each person uses 2 plates per meal?"""
    guests = 5
    meals_per_day = 3
    plates_per_person_per_meal = 2
    days = 4
    total_plates_used = guests * meals_per_day * plates_per_person_per_meal * days
    result = total_plates_used
    return result

print(solution())