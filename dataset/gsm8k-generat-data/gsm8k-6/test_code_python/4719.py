def solution():
    original_money = 48  # initial amount of money
    snacks_cost = 8  # amount spent on snacks
    remaining_money = 0.5 * original_money + 4  # remaining money after spending on accessories and snacks
    spent_on_accessories = original_money - snacks_cost - remaining_money  # amount spent on computer accessories
    result = spent_on_accessories
    return result

print(solution())