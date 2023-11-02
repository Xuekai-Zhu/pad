def solution():
    # Calculate the number of bowls delivered safely
    delivered_bowls = 638 - 12 - 15  # 12 bowls are lost and 15 bowls are broken

    # Calculate the total amount earned by delivering safely
    safe_delivery_amount = delivered_bowls * 3

    # Calculate the total amount earned after deducting $100 fee and lost/broken bowls fee
    total_earned = safe_delivery_amount - 4*(12+15) + 100

    result = total_earned
    return result

print(solution())