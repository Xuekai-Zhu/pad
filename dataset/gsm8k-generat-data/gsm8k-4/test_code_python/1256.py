def solution():
    """Conor can chop 12 eggplants, 9 carrots, and 8 potatoes in a day. If he works 4 times a week, how many vegetables can he chop?"""
    # Define the daily vegetable chopping capacity
    eggplants_per_day = 12
    carrots_per_day = 9
    potatoes_per_day = 8

    # Calculate the weekly vegetable chopping capacity
    total_veggies_per_day = eggplants_per_day + carrots_per_day + potatoes_per_day
    total_veggies_per_week = total_veggies_per_day * 4

    # return the result
    result = total_veggies_per_week
    return result

print(solution())