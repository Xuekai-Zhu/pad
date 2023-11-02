def solution():
    """Mark wants to tip his server 20% on a $200 check. If his friend agrees to kick in $10, how much should Mark add?"""
    # Define the check amount and tip percentage
    check_amount = 200
    tip_percentage = 0.20

    # Calculate the tip amount
    tip_amount = check_amount * tip_percentage

    # Add friend's contribution to the total tip amount
    total_tip_amount = tip_amount + 10

    # Display the amount Mark should add
    result = total_tip_amount - tip_amount
    return result

print(solution())