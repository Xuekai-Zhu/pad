def solution():
    """Megan is making food for a party. She has to spend 20 minutes preparing one dish in the oven. Each dish can feed 5 people. She spends 2 hours preparing as many of these dishes as she can for the party. How many people can she feed with these dishes?"""
    prep_time_per_dish = 20 # minutes 
    dishes_prepared = (2 * 60) // prep_time_per_dish  # 2 hours 
    people_per_dish = 5
    total_people_fed = dishes_prepared * people_per_dish
    result = total_people_fed
    return result

print(solution())