def solution():
    patricia_money = 6
    lisa_money = 5 * patricia_money
    charlotte_money = lisa_money / 2
    total_money = patricia_money + lisa_money + charlotte_money
    remaining_money = 100 - total_money
    result = remaining_money
    return result

print(solution())