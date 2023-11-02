def solution():
    # Calculate the amount left after buying ice cream
    remaining_money = 65 - 5

    # Calculate the amount spent on the t-shirt
    tshirt_cost = (1/2) * remaining_money
    remaining_money -= tshirt_cost

    # Calculate the amount deposited in the bank
    deposit = (1/5) * remaining_money
    remaining_money -= deposit

    result = remaining_money
    return result

print(solution())