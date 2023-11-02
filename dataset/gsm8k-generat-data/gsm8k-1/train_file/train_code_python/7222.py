def solution():
    """Méliès bought 2 kg of meat. The meat costs $82 per kilogram. Méliès has $180 in his wallet. How much money does he have left after paying for the meat?"""
    meat_price = 82
    meat_weight = 2
    total_price = meat_price * meat_weight
    wallet_balance = 180
    money_left = wallet_balance - total_price
    result = money_left
    return result

print(solution())