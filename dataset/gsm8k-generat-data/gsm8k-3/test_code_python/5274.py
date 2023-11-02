def solution():
    """Toms car gets 50 miles to the gallon. He drives 75 miles per day. If gas is $3 per gallon how much does he spend on gas in 10 days?"""
    # Find the number of gallons of gas used per day
    gallons_per_day = 75 / 50

    # Find the total cost of gas used in 10 days
    total_cost = gallons_per_day * 10 * 3

    # Display the total cost of gas for 10 days
    result = total_cost
    return result

print(solution())