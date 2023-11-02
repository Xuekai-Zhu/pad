def solution():
    """On Friday, Markeesha sold 30 boxes of crackers for her scout troop's fundraiser. On Saturday, she sold twice as many as on Friday. On Sunday, she sold 15 fewer than Saturday. How many boxes did she sell over the three days?"""
    # Define the number of boxes sold on Friday
    friday = 30

    # Define the number of boxes sold on Saturday
    saturday = friday * 2

    # Define the number of boxes sold on Sunday
    sunday = saturday - 15

    # Calculate the total number of boxes sold over the three days
    total = friday + saturday + sunday

    # return the result
    result = total
    return result

print(solution())