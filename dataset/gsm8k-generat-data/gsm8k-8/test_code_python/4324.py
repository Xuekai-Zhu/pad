def solution():
    # Calculate the total amount of money Carmela and her cousins have
    total_money = 7 + (4 * 2)

    # Calculate the amount of money each person should have
    equal_money = total_money / 5

    # Calculate the amount Carmela needs to give to each of her cousins
    amount_to_give = equal_money - 2

    result = amount_to_give
    return result

print(solution())