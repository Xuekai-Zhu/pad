def solution():
    """Méliès bought 2 kg of meat. The meat costs $82 per kilogram. Méliès has $180 in his wallet. How much money does he have left after paying for the meat?"""
    meat_cost = 82 * 2
    wallet_amount = 180
    remaining_amount = wallet_amount - meat_cost
    result = remaining_amount
    return result

print(solution())