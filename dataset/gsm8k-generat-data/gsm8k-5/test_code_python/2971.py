def solution():
    flies_per_day = 2  # The frog eats 2 flies every day
    flies_caught_morning = 5  # Betty catches 5 flies in the morning
    flies_caught_afternoon = 6  # Betty catches 6 flies in the afternoon, but 1 escapes

    # Calculate the total number of flies caught per day
    total_flies_caught_per_day = flies_caught_morning + flies_caught_afternoon - 1

    # Calculate the total number of flies caught in a week
    total_flies_caught_week = total_flies_caught_per_day * 7

    # Calculate the number of flies still needed for the whole week
    flies_still_needed = flies_per_day * 7 - total_flies_caught_week
    result = flies_still_needed
    return result

print(solution())