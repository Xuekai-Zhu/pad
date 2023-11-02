def solution():
    """Rachel makes $12.00 as a waitress in a coffee shop.  In one hour, she serves 20 different people and they all leave her a $1.25 tip.  How much money did she make in that hour?"""
    # Define the hourly rate and tip amount
    HOURLY_RATE = 12.00
    TIP_AMOUNT = 1.25

    # Calculate the total amount of tips
    total_tips = 20 * TIP_AMOUNT

    # Calculate Rachel's total earnings for the hour
    total_earnings = HOURLY_RATE + total_tips

    # Display Rachel's total earnings for the hour
    result = total_earnings
    return result

print(solution())