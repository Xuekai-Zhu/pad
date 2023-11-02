def solution():
    rica_share_fraction = 3/8
    rica_spent_fraction = 1/5
    rica_left = 300

    # Calculate the total prize money won by Rica's group
    rica_share = rica_left / (1 - rica_spent_fraction) # Rica's share after spending
    total_prize_money = rica_share / rica_share_fraction
    result = total_prize_money
    return result

print(solution())