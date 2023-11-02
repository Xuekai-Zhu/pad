def solution():
    """Greg has his own dog walking business. He charges $20 per dog plus $1 per minute per dog for walking the dog. If he walks one dog for 10 minutes, two dogs for 7 minutes and three dogs for 9 minutes, how much money, in dollars, does he earn?"""
    # Define the cost per dog and per minute
    DOG_COST = 20
    MINUTE_COST = 1

    # Define the number of dogs and minutes for each walk
    walk1_dogs = 1
    walk1_minutes = 10
    walk2_dogs = 2
    walk2_minutes = 7
    walk3_dogs = 3
    walk3_minutes = 9

    # Calculate the total cost for each walk
    walk1_cost = DOG_COST * walk1_dogs + MINUTE_COST * walk1_dogs * walk1_minutes
    walk2_cost = DOG_COST * walk2_dogs + MINUTE_COST * walk2_dogs * walk2_minutes
    walk3_cost = DOG_COST * walk3_dogs + MINUTE_COST * walk3_dogs * walk3_minutes

    # Calculate the total earnings for all the walks
    total_earnings = walk1_cost + walk2_cost + walk3_cost

    # Display the total earnings
    result = total_earnings
    return result

print(solution())