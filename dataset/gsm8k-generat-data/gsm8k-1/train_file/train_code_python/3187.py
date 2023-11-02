def solution():
    """Tom invites his parents and 3 siblings to his house. They each eat 3 times a day. How many plates do Tom and his guests use while they are there for the 4 days if each person uses 2 plates per meal?"""
    num_family_members = 5
    meals_per_day = 3
    days_staying = 4
    plates_per_meal = 2
    total_plates = num_family_members * meals_per_day * days_staying * plates_per_meal
    result = total_plates
    return result

print(solution())