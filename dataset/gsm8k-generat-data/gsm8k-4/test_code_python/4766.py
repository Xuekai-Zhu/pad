def solution():
    """A swarm of ants discovered a pile of sugar that spilled from a dropped bag. They begin to harvest it and carry it off to their anthill. Every hour, the ants remove 4 ounces of sugar. The bag of sugar held 24 ounces before it was dropped. After three hours, how many more hours will the ants need to harvest the remaining sugar?"""
    # Define the initial amount of sugar and the amount of sugar removed per hour
    INITIAL_SUGAR = 24
    SUGAR_REMOVED_PER_HOUR = 4

    # Calculate the amount of sugar remaining after 3 hours
    sugar_remaining = INITIAL_SUGAR - (SUGAR_REMOVED_PER_HOUR * 3)

    # Calculate the number of hours needed to remove the remaining sugar
    hours_needed = sugar_remaining / SUGAR_REMOVED_PER_HOUR

    # return the result
    result = hours_needed
    return result

print(solution())