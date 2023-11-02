def solution():
    # Calculate the total amount of money Carmela and her cousins have
    total_money = 7 + 4 * 2  # Carmela has $7 and each of her four cousins has $2

    # Calculate how much each person should have
    equal_amount = total_money / 5  # There are 5 people in total (Carmela and her 4 cousins)

    # Calculate how much Carmela needs to give to each of her cousins
    amount_to_give = equal_amount - 2  # Each of her cousin already has $2

    result = amount_to_give
    return result

print(solution())