def solution():
    """Jon runs a website where he gets paid for every person who visits. He gets paid $0.10 for every person who visits. Each hour he gets 50 visits. His website operates 24 hours a day. How many dollars does he make in a 30 day month?"""
    # Calculate the number of visits Jon gets in one day
    visits_per_day = 24 * 50

    # Calculate the number of visits Jon gets in one month
    visits_per_month = visits_per_day * 30

    # Calculate Jon's earnings in one month
    earnings_per_month = visits_per_month * 0.10

    # Display Jon's earnings in one month
    result = earnings_per_month
    return result

print(solution())