def solution():
    """Gabby is saving money to buy a new makeup set. The makeup set costs $65 and she already has $35. Gabby’s mom gives her an additional $20. How much money does Gabby need to buy the set?"""
    cost_of_makeup_set = 65
    existing_money = 35
    additional_money = 20
    total_money = existing_money + additional_money
    money_needed = cost_of_makeup_set - total_money
    result = money_needed
    return result

print(solution())