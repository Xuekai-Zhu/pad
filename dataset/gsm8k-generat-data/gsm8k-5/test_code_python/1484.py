def solution():
    remaining_money = 15  # Lucy is only left with $15 at the end
    spent_money = remaining_money / 0.25 - remaining_money  # Lucy spent one-fourth of the remainder, so she spent 3/4 of the remainder
    original_money = (remaining_money + spent_money) / (1 - 1/3)  # Lucy lost one-third of her money, so only has 2/3 left

    result = original_money
    return result

print(solution())