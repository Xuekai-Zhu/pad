def solution():
    """Mary went to the store to buy fruit. Apples cost $1, oranges cost $2, and bananas cost $3. For every 5 fruits that customers buy, the store offers a $1 discount. Mary buys 5 apples, 3 oranges, and 2 bananas. How much will she pay?"""
    # Define the prices of each fruit
    APPLE_PRICE = 1
    ORANGE_PRICE = 2
    BANANA_PRICE = 3

    # Define the number of each fruit Mary buys
    num_apples = 5
    num_oranges = 3
    num_bananas = 2

    # Calculate the total number of fruit that Mary buys
    total_fruit = num_apples + num_oranges + num_bananas

    # Calculate the total cost before discount
    total_cost = (num_apples * APPLE_PRICE) + (num_oranges * ORANGE_PRICE) + (num_bananas * BANANA_PRICE)

    # Calculate the number of discounts Mary is eligible for
    num_discounts = total_fruit // 5

    # Calculate the total discount
    total_discount = num_discounts * 1

    # Calculate the final cost after discount
    final_cost = total_cost - total_discount

    # Display the final cost
    result = final_cost
    return result

print(solution())