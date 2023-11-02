def solution():
    cory_money = 20
    candy_price = 49
    num_candies = 2

    # Calculate the total cost of two packs of candies
    total_cost = candy_price * num_candies

    # Calculate how much more money Cory needs to buy the candies
    money_needed = total_cost - cory_money
    result = money_needed
    return result

print(solution())