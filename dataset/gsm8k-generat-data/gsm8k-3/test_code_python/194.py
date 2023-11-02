def solution():
    """ Mr. Grey is purchasing gifts for his family. So far he has purchased
    3 polo shirts for $26 each; 2 necklaces for $83 each; and 1 computer game for
    $90. Since Mr. Grey purchased all those using his credit card, he received
    a $12 rebate. What is the total cost of the gifts after the rebate?"""
    # Define the prices of the gifts
    polo_price = 26
    necklace_price = 83
    game_price = 90

    # Calculate the total cost before rebate
    total_cost = 3 * polo_price + 2 * necklace_price + game_price

    # Subtract the rebate from the total cost
    total_cost -= 12

    result = total_cost
    return result

print(solution())