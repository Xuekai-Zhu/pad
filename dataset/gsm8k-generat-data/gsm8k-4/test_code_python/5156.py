def solution():
    """A man used to have 39 cows but last year 25 of them died and he sold 6 of them. 
    This year the number of the cows increased by 24 and the man bought 43 more. 
    His friend gave him 8 cows as a gift. How many cows does the man have now?"""
    # Define the initial number of cows
    initial_cows = 39

    # Calculate the number of cows left after last year's losses and sales
    cows_last_year = initial_cows - 25 - 6

    # Calculate the number of cows this year, including purchases and gifts
    cows_this_year = cows_last_year + 24 + 43 + 8

    # return the result
    result = cows_this_year
    return result

print(solution())