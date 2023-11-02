def solution():
    """Phillip's mother asked him to go to the supermarket to buy some things and gave him $95, so he spent $14 on oranges, $25 on apples and $6 on candy. How much money does he have left?"""
    initial_money = 95
    spent_money = 14 + 25 + 6
    remaining_money = initial_money - spent_money
    result = remaining_money
    return result

print(solution())