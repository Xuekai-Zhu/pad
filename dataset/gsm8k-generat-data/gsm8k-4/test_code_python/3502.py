def solution():
    """Spike the bearded dragon eats crickets to get protein in his diet. He hunts 5 crickets every morning and three times that over the afternoon and evening, munching on leafy greens and other vegetation in between. How many crickets does Spike hunt per day?"""
    # Define the number of crickets Spike hunts in the morning
    morning_crickets = 5

    # Define the multiplier for the afternoon and evening hunts
    afternoon_multiplier = 3

    # Calculate the number of crickets Spike hunts in the afternoon and evening
    afternoon_crickets = morning_crickets * afternoon_multiplier

    # Calculate the total number of crickets Spike hunts per day
    total_crickets = morning_crickets + afternoon_crickets

    result = total_crickets
    return result

print(solution())