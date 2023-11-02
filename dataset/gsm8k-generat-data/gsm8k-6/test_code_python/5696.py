def solution():
    # Calculate the total number of phrases the parrot has learned, including the three it knew when Georgina bought it
    total_phrases = 17 + 3  # the parrot already knew three phrases when Georgina bought it, and has learned 2 more phrases every week since then

    # Calculate the number of weeks Georgina has had the parrot
    weeks = (total_phrases - 3) / 2

    # Calculate the number of days Georgina has had the parrot
    days = weeks * 7

    result = days
    return result

print(solution())