def solution():
    """Spike the bearded dragon eats crickets to get protein in his diet. He hunts 5 crickets every morning and three times that over the afternoon and evening, munching on leafy greens and other vegetation in between. How many crickets does Spike hunt per day?"""
    # Define the number of crickets hunted in the morning
    MORNING_CRICKETS = 5

    # Calculate the number of crickets hunted in the afternoon and evening
    AFTERNOON_EVENING_CRICKETS = MORNING_CRICKETS * 3

    # Calculate the total number of crickets hunted per day
    total_cricket_hunts = MORNING_CRICKETS + AFTERNOON_EVENING_CRICKETS

    # Display the total number of crickets hunted per day
    result = total_cricket_hunts
    return result

print(solution())