def solution():
    check_total = 200  # The total amount of the check is $200
    tip_percentage = 0.2  # Mark wants to tip his server 20%
    tip_amount = check_total * tip_percentage  # Calculate the amount of the tip
    total_with_tip = check_total + tip_amount  # Calculate the total amount with the tip
    friend_contribution = 10  # Mark's friend is contributing $10
    total_with_friend = total_with_tip + friend_contribution  # Calculate the total with the friend's contribution

    # Calculate the amount Mark needs to add
    mark_contribution = total_with_friend - check_total
    result = mark_contribution
    return result

print(solution())