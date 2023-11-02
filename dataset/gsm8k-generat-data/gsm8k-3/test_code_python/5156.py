def solution():
    """A man used to have 39 cows but last year 25 of them died and he sold 6 of them. This year the number of the cows increased by 24 and the man bought 43 more. His friend gave him 8 cows as a gift. How many cows does the man have now?"""
    # Define the initial number of cows the man had
    initial_cows = 39

    # Calculate the number of cows left after deaths and sales
    cows_after_deaths_and_sales = initial_cows - 25 - 6

    # Calculate the number of cows the man has this year
    cows_this_year = cows_after_deaths_and_sales + 24 + 43 + 8

    # Display the current number of cows
    result = cows_this_year
    return result

print(solution())