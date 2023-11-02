def solution():
    """A family just bought a newborn puppy that must eat a special type of dog food until it is 1 year old. 
    The puppy needs to eat 2 ounces of this special dog food per day during the first 60 days of its life. 
    After that, it needs to eat 4 ounces per day of the special food until it is old enough to eat regular dog food. 
    If the special dog food is only sold in 5-pound bags, and there are 16 ounces in a pound, 
    how many bags will the family need to buy to feed the puppy until it is old enough to eat regular dog food?"""
    first_60_days = 2 * 60 
    after_60_days = 4 * (365-60) 
    total_food = first_60_days + after_60_days
    ounces_per_bag = 5 * 16
    bags_needed = total_food / ounces_per_bag
    result = bags_needed
    return result

print(solution())