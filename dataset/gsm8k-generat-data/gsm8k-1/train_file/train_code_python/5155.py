def solution():
    """A man used to have 39 cows but last year 25 of them died and he sold 6 of them.
    This year the number of the cows increased by 24 and the man bought 43 more.
    His friend gave him 8 cows as a gift. How many cows does the man have now?"""
    original_cows = 39
    cows_after_death_and_sale = original_cows - 25 - 6
    cows_this_year = cows_after_death_and_sale + 24 + 43 + 8
    result = cows_this_year
    return result

print(solution())