def solution():
    """Kenneth spent 10% of this earnings this week on a new joystick. If he is left with $405, how much were his earnings?"""
    # Define the percentage spent on the joystick
    percent_spent = 0.1

    # Calculate the amount spent on the joystick
    amount_spent = percent_spent * earnings

    # Calculate the remaining earnings after the purchase of the joystick
    remaining_earnings = earnings - amount_spent

    # Use the remaining earnings to find the original earnings
    original_earnings = remaining_earnings / 0.9

    result = original_earnings
    return result

print(solution())