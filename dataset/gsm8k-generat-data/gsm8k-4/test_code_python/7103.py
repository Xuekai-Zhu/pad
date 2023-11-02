def solution():
    """Harry decided to buy some balloons for his friend's birthday party. One balloon costs $0.5, and a pack of 10 balloons is cheaper and costs only $3. Finally, Harry wants to bring to the party exactly 14 balloons. How much did he need to pay for them?"""
    # Define the price of one balloon and the price of a pack of 10 balloons
    single_price = 0.5
    pack_price = 3

    # Calculate the number of packs needed to buy 14 balloons
    packs = 14 // 10

    # Calculate the number of single balloons needed to buy 14 balloons
    singles = 14 % 10

    # Calculate the total cost of buying the balloons
    total_cost = packs * pack_price + singles * single_price

    # Return the result
    result = total_cost
    return result

print(solution())