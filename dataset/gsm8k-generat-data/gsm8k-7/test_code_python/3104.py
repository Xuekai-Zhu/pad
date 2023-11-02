def solution():
    check_amount = 200
    tip_percent = 0.20  # 20% tip
    friend_contribution = 10

    # Calculate the amount of the tip
    tip_amount = check_amount * tip_percent

    # Calculate the total amount Mark needs to pay, including the tip and friend's contribution
    total_amount = check_amount + tip_amount + friend_contribution

    # Calculate how much Mark needs to add to cover the tip
    mark_contribution = tip_amount - friend_contribution

    result = mark_contribution
    return result

print(solution())