def solution():
    """Billy is buying some candy with $10 his father gave him. The candy costs $1.5 a pound. After buying candy, he takes half his change and spends it on gumballs, which cost $.05 each. If he bought 40 gumballs, how many pounds of candy did he buy?"""
    money_available = 10
    candy_price = 1.5
    candy_bought = (money_available - (money_available/2)) / candy_price
    result = candy_bought
    return result

print(solution())