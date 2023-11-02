def solution():
    """Sammy has 8 gifts to wrap. Each gift requires 1.5 meters of ribbon. Unfortunately, she has no available ribbon so Tom let her use his 15-meter long ribbon. How many meters of ribbon will be left from Tom's ribbon?"""
    # Define the number of gifts and the length of ribbon each gift requires
    NUM_GIFTS = 8
    RIBBON_PER_GIFT = 1.5

    # Define the length of Tom's ribbon
    TOMS_RIBBON_LENGTH = 15

    # Calculate the total length of ribbon needed for all the gifts
    total_ribbon_length = NUM_GIFTS * RIBBON_PER_GIFT

    # Calculate the length of ribbon that will be left from Tom's ribbon
    ribbon_left = TOMS_RIBBON_LENGTH - total_ribbon_length

    # Display the length of ribbon left
    result = ribbon_left
    return result

print(solution())