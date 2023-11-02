def solution():
    """Sammy has 8 gifts to wrap. Each gift requires 1.5 meters of ribbon. Unfortunately, she has no available ribbon so Tom let her use his 15-meter long ribbon. How many meters of ribbon will be left from Tom's ribbon?"""
    # Define the number of gifts and the amount of ribbon required per gift
    num_gifts = 8
    ribbon_per_gift = 1.5

    # Calculate the total amount of ribbon needed
    total_ribbon = num_gifts * ribbon_per_gift

    # Calculate the amount of ribbon left from Tom's ribbon
    ribbon_left = 15 - total_ribbon

    # Return the result
    result = ribbon_left
    return result

print(solution())