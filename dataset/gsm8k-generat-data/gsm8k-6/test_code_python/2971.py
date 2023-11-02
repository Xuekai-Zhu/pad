def solution():
    # Calculate the total number of flies caught by Betty in a day
    flies_per_day = 5 + 6 - 1  # Betty catches 5 flies in the morning, 6 in the afternoon, but 1 escapes when she removes the lid

    # Calculate the total number of flies caught in a week
    flies_per_week = flies_per_day * 7  # Betty wants to gather the whole week's food for her frog

    # Calculate the number of additional flies Betty needs
    additional_flies = 2 * 7 - flies_per_day  # the frog eats 2 flies every day, so Betty needs 2 * 7 = 14 flies in a week
                                             # Subtract the flies already caught to find how many more she needs
    result = additional_flies
    return result

print(solution())