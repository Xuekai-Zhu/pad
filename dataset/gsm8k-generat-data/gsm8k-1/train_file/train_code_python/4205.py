def solution():
    """A family just bought a newborn puppy that must eat a special type of dog food until it is 1 year old. The puppy needs to eat 2 ounces of this special dog food per day during the first 60 days of its life. After that, it needs to eat 4 ounces per day of the special food until it is old enough to eat regular dog food. If the special dog food is only sold in 5-pound bags, and there are 16 ounces in a pound, how many bags will the family need to buy to feed the puppy until it is old enough to eat regular dog food?"""
    
    # number of days the puppy eats 2 ounces per day
    first_60_days = 60
    
    # number of days the puppy eats 4 ounces per day
    remaining_days = 365 - 60
    
    # total amount of food needed in ounces
    total_food = (first_60_days * 2) + (remaining_days * 4)
    
    # convert total food to pounds
    total_food_pounds = total_food / 16
    
    # calculate number of 5-pound bags needed and round up to nearest whole number
    bags_needed = math.ceil(total_food_pounds / 5)
    
    return bags_needed

print(solution())