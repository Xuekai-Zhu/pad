def solution():
    """Bill the miner discovers a vein of fool's gold. He successfully sells 8 ounces to a merchant, but when he tries to sell to the sheriff he's arrested, fined $50 and run out of town on a rail. If Bill earned $9 for every ounce of fool's gold he sold, how much money is he left with?"""
    gold_price = 9
    sold_gold = 8
    total_earned = sold_gold * gold_price
    fine = 50
    money_left = total_earned - fine
    result = money_left
    return result

print(solution())