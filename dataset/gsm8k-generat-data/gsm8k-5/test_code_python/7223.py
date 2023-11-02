def solution():
    meat_cost = 2 * 82  # 2 kg of meat at $82 per kg
    total_cost = meat_cost
    wallet_amount = 180  # Méliès has $180 in his wallet

    # Calculate the money left after paying for the meat
    remaining_money = wallet_amount - total_cost
    result = remaining_money
    return result

print(solution())