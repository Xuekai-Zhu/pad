def solution():
    """Megan is making food for a party. She has to spend 20 minutes preparing one dish in the oven. Each dish can feed 5 people. She spends 2 hours preparing as many of these dishes as she can for the party. How many people can she feed with these dishes?"""
    dish_time = 20
    dishes_per_hour = 60 / dish_time
    dishes_prepared = 2 * dishes_per_hour
    people_fed = dishes_prepared * 5
    result = people_fed
    return result

print(solution())