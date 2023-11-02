def solution():
    ricas_share_fraction = 3/8  # Rica got 3/8 of the prize money
    ricas_share = ricas_share_fraction * total_prize_money  # Rica's share of the prize money
    ricas_share_after_spending = ricas_share - (1/5) * ricas_share  # Rica is left with $300 after spending 1/5 of her share
    # Solve for the total prize money
    total_prize_money = ricas_share_after_spending / ricas_share_fraction
    result = total_prize_money
    return result

print(solution())