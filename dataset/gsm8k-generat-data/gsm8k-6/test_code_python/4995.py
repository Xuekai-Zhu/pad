def solution():
    # Calculate the total number of songs John buys in a month
    songs_per_month = (20 * 60) / 3  # 20 hours of music per month, with each song being 3 minutes long

    # Calculate the cost of the songs John buys in a month
    cost_per_month = songs_per_month * 0.5  # each song costs $0.50

    # Calculate the cost of the songs John buys in a year
    cost_per_year = cost_per_month * 12  # 12 months in a year

    result = cost_per_year
    return result

print(solution())