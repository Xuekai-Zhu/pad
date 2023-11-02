def solution():
    """Flies are Betty's frog's favorite food. Every day the frog eats 2 flies. Betty puts the flies she finds in a bottle. In the morning Betty catches 5 flies inside a bottle, and in the afternoon she catches 6 more, but when she removes the lid, one escapes. Betty wants to gather the whole week's food for her frog. How many more flies does she need?"""
    flies_per_day = 2
    morning_catch = 5
    afternoon_catch = 6 - 1  # one escaped
    daily_total = morning_catch + afternoon_catch
    flies_needed_per_week = flies_per_day * 7
    flies_collected_per_week = daily_total * 7
    flies_needed = flies_needed_per_week - flies_collected_per_week
    result = flies_needed
    return result

print(solution())