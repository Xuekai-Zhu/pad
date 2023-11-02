def solution():
    """Gabby is saving money to buy a new makeup set. The makeup set costs $65 and she already has $35. Gabby’s mom gives her an additional $20. How much money does Gabby need to buy the set?"""
    makeup_set_cost = 65
    current_savings = 35 + 20
    money_needed = makeup_set_cost - current_savings
    result = money_needed
    return result

print(solution())