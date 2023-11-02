def solution():
    """Jerry works five days a week as a waiter and earns a variable amount of tips every night. The past four nights, he earned $20, $60, $15, and $40. How much does he need to earn tonight if he wants to make an average of $50 in tips per night?"""
    # Define the current total tips Jerry has earned
    current_tips = 20 + 60 + 15 + 40

    # Define the number of days Jerry has worked
    days_worked = 4

    # Define the target average tips per night
    target_average = 50

    # Calculate the total tips Jerry needs to earn by the end of the week
    total_tips_needed = target_average * 5 - current_tips

    # Calculate the tips Jerry needs to earn tonight
    tips_needed = total_tips_needed / (5 - days_worked)

    result = tips_needed
    return result

print(solution())