def solution():
    """A man used to have 39 cows but last year 25 of them died and he sold 6 of them. This year the number of the cows increased by 24 and the man bought 43 more. His friend gave him 8 cows as a gift. How many cows does the man have now?"""
    initial_cows = 39
    cows_died = 25
    cows_sold = 6
    current_cows = initial_cows - cows_died - cows_sold
    current_cows += 24
    current_cows += 43
    current_cows += 8
    result = current_cows
    return result

print(solution())