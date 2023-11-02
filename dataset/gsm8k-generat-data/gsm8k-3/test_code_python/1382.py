def solution():
    """Your video streaming subscription costs $14 a month. If you're evenly splitting the cost with your friend, how much do you pay in total after the first year for this service?"""
    # Define the cost of the subscription per month
    MONTHLY_COST = 14

    # Calculate the total cost of the subscription for a year
    total_cost = MONTHLY_COST * 12

    # Calculate each person's share of the cost
    share = total_cost / 2

    # Display each person's share of the cost
    result = share
    return result

print(solution())