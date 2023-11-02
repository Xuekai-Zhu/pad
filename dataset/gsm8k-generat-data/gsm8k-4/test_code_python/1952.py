def solution():
    """Sol sells candy bars to raise money for her softball team. On the first day, she sells ten candy bars and sells four more candy bars than she sold the previous day each day afterward. If she sells six days a week and each candy bar costs 10 cents, how much will she earn in a week in dollars?"""
    # Define the initial number of candy bars sold and the number of days in a week
    initial_candy_bars = 10
    days_in_week = 6

    # Calculate the total number of candy bars sold in a week
    total_candy_bars = initial_candy_bars

    for i in range(1, days_in_week):
        candy_bars_today = initial_candy_bars + 4 * i
        total_candy_bars += candy_bars_today

    # Calculate the earnings from selling candy bars in a week
    earnings_in_cents = total_candy_bars * 10  

    # Convert the earnings to dollars
    earnings_in_dollars = earnings_in_cents / 100

    # Return the result
    result = earnings_in_dollars
    return result

print(solution())