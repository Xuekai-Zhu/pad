def solution():
    """Cassie is an athletic person and tries to drink at least 12 cups of water a day to stay hydrated while being active. Her water bottle holds 16 ounces. There are 8 ounces of water in a cup. How many times does Cassie have to refill her water bottle a day to make sure she drinks 12 cups?"""
    # Define the number of cups Cassie wants to drink
    cups_per_day = 12

    # Calculate the total number of ounces Cassie needs to drink per day
    ounces_per_day = cups_per_day * 8

    # Calculate the number of times Cassie needs to refill her water bottle per day
    refills_per_day = ounces_per_day / 16

    # Round up to the nearest whole number
    refills_per_day = math.ceil(refills_per_day)

    result = refills_per_day
    return result

print(solution())