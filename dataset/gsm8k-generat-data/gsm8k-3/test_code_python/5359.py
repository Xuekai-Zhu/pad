def solution():
    """Cassie is an athletic person and tries to drink at least 12 cups of water a day to stay hydrated while being active. Her water bottle holds 16 ounces. There are 8 ounces of water in a cup. How many times does Cassie have to refill her water bottle a day to make sure she drinks 12 cups?"""
    # Define the number of ounces in a cup and in Cassie's water bottle
    OUNCES_PER_CUP = 8
    OUNCES_PER_BOTTLE = 16

    # Define the number of cups Cassie wants to drink
    cups_per_day = 12

    # Calculate the number of ounces Cassie wants to drink
    ounces_per_day = cups_per_day * OUNCES_PER_CUP

    # Calculate the number of times Cassie needs to refill her water bottle
    refills_per_day = ounces_per_day / OUNCES_PER_BOTTLE

    # Display the number of times Cassie needs to refill her water bottle
    result = refills_per_day
    return result

print(solution())