def solution():
    """Cassie is an athletic person and tries to drink at least 12 cups of water a day to stay hydrated while being active. Her water bottle holds 16 ounces. There are 8 ounces of water in a cup. How many times does Cassie have to refill her water bottle a day to make sure she drinks 12 cups?"""
    cups_per_day = 12
    ounces_per_cup = 8
    ounces_per_bottle = 16
    cups_per_bottle = ounces_per_bottle / ounces_per_cup
    refills_per_day = cups_per_day / cups_per_bottle
    result = refills_per_day
    return result

print(solution())