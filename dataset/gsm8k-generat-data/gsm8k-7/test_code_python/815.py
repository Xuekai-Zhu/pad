def solution():
    bingley_starting = 5
    kelly_starting = 16

    # Calculate how many bracelets Kelly gives to Bingley
    kelly_gives = kelly_starting / 4

    # Calculate how many bracelets Bingley has after receiving Kelly's bracelets.
    bingley_after_kelly = bingley_starting + kelly_gives

    # Calculate how many bracelets Bingley gives to his little sister
    bingley_gives = bingley_after_kelly / 3

    # Calculate how many bracelets Bingley has left
    bingley_remaining = bingley_after_kelly - bingley_gives

    result = bingley_remaining
    return result

print(solution())