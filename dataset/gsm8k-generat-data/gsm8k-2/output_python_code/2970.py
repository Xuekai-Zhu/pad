def solution():
    """Flies are Betty's frog's favorite food. Every day the frog eats 2 flies. Betty puts the flies she finds in a bottle. In the morning Betty catches 5 flies inside a bottle, and in the afternoon she catches 6 more, but when she removes the lid, one escapes. Betty wants to gather the whole week's food for her frog. How many more flies does she need?"""
    daily_flies = 5 + 5 + 6 - 1
    weekly_flies = daily_flies * 7
    frog_food = 2 * 7
    more_flies = weekly_flies - frog_food
    result = more_flies
    return result

print(solution())