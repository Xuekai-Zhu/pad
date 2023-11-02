def solution():
    """Flies are Betty's frog's favorite food. Every day the frog eats 2 flies. Betty puts the flies she finds in a bottle. In the morning Betty catches 5 flies inside a bottle, and in the afternoon she catches 6 more, but when she removes the lid, one escapes. Betty wants to gather the whole week's food for her frog. How many more flies does she need?"""
    # Calculate the number of flies caught in a day and the number of flies eaten by the frog
    flies_per_day = 5 + 5 + 6 - 1
    flies_eaten_per_day = 2

    # Calculate the number of flies needed for the whole week
    flies_needed_per_week = flies_eaten_per_day * 7

    # Calculate the number of additional flies needed
    additional_flies_needed = flies_needed_per_week - flies_per_day * 7

    # Return the result
    result = additional_flies_needed
    return result

print(solution())