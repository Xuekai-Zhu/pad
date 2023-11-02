def solution():
    # Calculate the total amount without tips
    lawn_count = 16
    lawn_cost = 33
    total_lawn_cost = lawn_count * lawn_cost

    # Calculate the total amount of tips
    tip_count = 3
    tip_amount = 10
    total_tip_amount = tip_count * tip_amount

    # Calculate the total earnings
    total_earnings = total_lawn_cost + total_tip_amount
    result = total_earnings
    return result

print(solution())