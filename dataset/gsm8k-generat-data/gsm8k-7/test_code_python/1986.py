def solution():
    total_money = 240
    samuel_share = total_money * (3/4)

    # Calculate the amount spent on drinks
    drinks_cost = total_money * (3/4) * (1/5)

    # Calculate how much Samuel has left
    samuel_left = samuel_share - drinks_cost
    result = samuel_left
    return result

print(solution())