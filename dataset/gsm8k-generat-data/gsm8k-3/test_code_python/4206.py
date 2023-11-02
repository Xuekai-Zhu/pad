def solution():
    """A family just bought a newborn puppy that must eat a special type of dog food until it is 1 year old.  The puppy needs to eat 2 ounces of this special dog food per day during the first 60 days of its life.  After that, it needs to eat 4 ounces per day of the special food until it is old enough to eat regular dog food.  If the special dog food is only sold in 5-pound bags, and there are 16 ounces in a pound, how many bags will the family need to buy to feed the puppy until it is old enough to eat regular dog food?"""
    # Define the number of ounces of food per day
    FIRST_60_DAYS = 2
    AFTER_60_DAYS = 4

    # Calculate the number of ounces of food the puppy needs in the first 60 days
    first_60_days_ounces = FIRST_60_DAYS * 60

    # Calculate the number of ounces of food the puppy needs after the first 60 days
    after_60_days_ounces = AFTER_60_DAYS * (365 - 60)

    # Calculate the total number of ounces of food the puppy needs
    total_ounces = first_60_days_ounces + after_60_days_ounces

    # Convert the total number of ounces to pounds
    total_pounds = total_ounces / 16

    # Calculate the number of 5-pound bags needed
    bags_needed = math.ceil(total_pounds / 5)

    # Display the number of bags needed
    result = bags_needed
    return result

print(solution())