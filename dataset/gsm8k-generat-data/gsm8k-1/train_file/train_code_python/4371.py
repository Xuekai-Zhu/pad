def solution():
    """Cory has $20.00 and she wants to buy two packs of candies that cost $49.00 each. How much money does Cory need so she will be able to buy the pack of candies?"""
    available_money = 20
    candy_cost = 49
    total_cost = candy_cost * 2
    needed_money = total_cost - available_money
    result = needed_money
    return result

print(solution())