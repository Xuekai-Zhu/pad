def solution():
    # Calculate the total time for three articles
    total_time = 4 * 60

    # Calculate the total number of words for three articles
    total_words = 3 * 60 * 10

    # Calculate the total earnings for three articles
    total_earnings = (total_words * 0.1) + (3 * 60)

    # Calculate the earnings per hour
    earnings_per_hour = total_earnings / 4
    result = earnings_per_hour
    return result

print(solution())