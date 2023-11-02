def solution():
    day_before_yesterday = 50  # The day before had 50 buyers
    yesterday = day_before_yesterday / 2 + 40  # Yesterday had half the buyers as day before + 40 more
    today = yesterday + day_before_yesterday + 40  # Today had 40 more buyers than yesterday and day before combined

    # Calculate the total number of buyers who've visited the store in the three days
    total_buyers = day_before_yesterday + yesterday + today
    result = total_buyers
    return result

print(solution())