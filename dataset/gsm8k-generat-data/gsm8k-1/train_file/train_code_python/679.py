def solution():
    """Cecil has $600. Catherine has $250 less than twice as much as Cecil while Carmela has $50 more than twice Cecil's money. How much money do they have altogether?"""
    cecil_money = 600
    catherine_money = 2 * cecil_money - 250
    carmela_money = 2 * cecil_money + 50
    total_money = cecil_money + catherine_money + carmela_money
    result = total_money
    return result

print(solution())