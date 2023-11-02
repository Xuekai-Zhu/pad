def solution():
    """A cup of dog food weighs 1/4 of a pound. If Mike has 2 dogs that each eat 6 cups of dog food twice a day how many 20 pound bags of dog food does he need to buy a month?"""
    # Define the weight of one cup of dog food
    cup_weight = 1/4

    # Define the number of dogs and cups of food per day
    num_dogs = 2
    num_cups_per_day = 6
    num_meals_per_day = 2

    # Calculate the total weight of food consumed in a day
    daily_food_weight = num_dogs * num_cups_per_day * cup_weight * num_meals_per_day

    # Calculate the weight of food consumed in a month
    monthly_food_weight = daily_food_weight * 30

    # Calculate the number of 20 pound bags of food needed
    bags_needed = monthly_food_weight / 20

    # Round up to the nearest whole bag
    bags_needed = math.ceil(bags_needed)

    # return the result
    result = bags_needed
    return result

print(solution())