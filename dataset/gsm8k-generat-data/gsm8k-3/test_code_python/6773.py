def solution():
    """Jerry works five days a week as a waiter and earns a variable amount of tips every night. The past four nights, he earned $20, $60, $15, and $40. How much does he need to earn tonight if he wants to make an average of $50 in tips per night?"""
    # Define the number of days Jerry works in a week and his desired average nightly tips
    NUM_DAYS = 5
    DESIRED_AVG_TIPS = 50

    # Define the total amount of tips Jerry has earned so far this week
    total_tips = 20 + 60 + 15 + 40

    # Calculate the total amount of tips Jerry needs to earn to achieve his desired average
    desired_total_tips = NUM_DAYS * DESIRED_AVG_TIPS
    needed_tips = desired_total_tips - total_tips

    # Display the amount of tips Jerry needs to earn tonight
    result = needed_tips
    return result

print(solution())