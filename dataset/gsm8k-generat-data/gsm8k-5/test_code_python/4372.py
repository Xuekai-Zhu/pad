def solution():
    price_of_one_pack = 49.00  # Price of one pack of candies
    packs_to_buy = 2  # Number of packs to buy
    current_money = 20.00  # Current amount of money Cory has

    # Calculate the total cost of the candy packs
    total_cost = price_of_one_pack * packs_to_buy

    # Calculate the remaining amount of money Cory needs to buy the candy packs
    remaining_money = total_cost - current_money
    result = remaining_money
    return result

print(solution())