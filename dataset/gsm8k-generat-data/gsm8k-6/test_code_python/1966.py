def solution():
    # Calculate the total earned from selling the clothes
    total_earned = (3*5) + (5*3)  # 3 pairs of pants sold for $5 each and 5 pairs of shorts sold for $3 each
    remaining_money = 30 - (2*10)  # Selina spent $20 on 2 shirts she bought
    num_shirts = remaining_money / 4  # each shirt sold for $4
    result = num_shirts
    return result

print(solution())