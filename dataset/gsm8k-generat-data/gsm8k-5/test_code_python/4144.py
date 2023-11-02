def solution():
    budget = 32  # You have 32$ to spend on groceries
    bread_price = 3  # The price of bread is 3$
    candy_price = 2  # The price of a candy bar is 2$

    # Calculate how much money is left after buying bread and candy
    money_left = budget - bread_price - candy_price

    # Calculate the price of the turkey
    turkey_price = money_left / 3

    # Calculate how much money is left after buying the turkey
    money_left = money_left - turkey_price

    result = money_left
    return result

print(solution())