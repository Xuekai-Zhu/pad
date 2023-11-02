def solution():
    """Cory has $20.00 and she wants to buy two packs of candies that cost $49.00 each. How much money does Cory need so she will be able to buy the pack of candies?"""
    cory_money = 20
    candy_pack_cost = 49
    total_cost = candy_pack_cost * 2
    money_needed = total_cost - cory_money
    result = money_needed
    return result

print(solution())