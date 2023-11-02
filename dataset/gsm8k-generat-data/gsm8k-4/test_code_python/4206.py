def solution():
    """A family just bought a newborn puppy that must eat a special type of dog food until it is 1 year old. The puppy needs to eat 2 ounces of this special dog food per day during the first 60 days of its life. After that, it needs to eat 4 ounces per day of the special food until it is old enough to eat regular dog food. If the special dog food is only sold in 5-pound bags, and there are 16 ounces in a pound, how many bags will the family need to buy to feed the puppy until it is old enough to eat regular dog food?"""
    
    # Define the number of days during which the puppy needs to eat 2 ounces of special dog food
    first_60_days = 60

    # Define the number of days during which the puppy needs to eat 4 ounces of special dog food
    remaining_days = 365 - first_60_days

    # Calculate the total amount of special dog food needed
    total_food = (first_60_days * 2) + (remaining_days * 4)

    # Convert the total amount of special dog food to pounds
    total_food_pounds = total_food / 16

    # Calculate the number of 5-pound bags needed to feed the puppy
    bags_needed = total_food_pounds / 5

    # Round up to the nearest whole bag
    bags_needed = math.ceil(bags_needed)

    # Return the result
    result = bags_needed
    return result

print(solution())