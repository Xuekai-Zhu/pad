def solution():
    """Cathy has $12 left in her wallet. Her dad sent her $25 for her weekly consumption while her mom sent her twice the amount her dad sent her. How much money does Cathy have now?"""
    starting_money = 12
    dad_money = 25
    mom_money = 2 * dad_money
    total_money = starting_money + dad_money + mom_money
    result = total_money
    return result

print(solution())