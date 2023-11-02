def solution():
    # Calculate the total amount of money among Carmela and her cousins
    total_money = 7 + 4 * 2

    # Calculate the amount of money each person should have after equal distribution
    equal_money = total_money / 5

    # Calculate the amount of money Carmela needs to give to each cousin
    amount_to_give = 7 - equal_money

    result = amount_to_give
    return result

print(solution())