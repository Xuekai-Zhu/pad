def solution():
    """Mark wants to tip his server 20% on a $200 check. If his friend agrees to kick in $10, how much should Mark add?"""
    # Define the check amount and the desired tip percentage
    check_amount = 200
    tip_percentage = 0.2

    # Calculate the amount of the tip
    tip_amount = check_amount * tip_percentage

    # Add the amount from Mark's friend
    total_tip_amount = tip_amount + 10

    # Calculate the total amount Mark should pay
    total_amount = check_amount + total_tip_amount

    # Calculate the amount Mark should add
    mark_should_add = total_tip_amount - tip_amount

    # return the result
    result = mark_should_add
    return result

print(solution())