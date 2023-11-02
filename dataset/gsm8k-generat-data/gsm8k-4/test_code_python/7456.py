def solution():
    """Mary went to the store to buy fruit. Apples cost $1, oranges cost $2, and bananas cost $3. For every 5 fruits that customers buy, the store offers a $1 discount. Mary buys 5 apples, 3 oranges, and 2 bananas. How much will she pay?"""
    # Define the prices of fruit
    apple_price = 1
    orange_price = 2
    banana_price = 3

    # Define the number of each fruit that Mary buys
    num_apples = 5
    num_oranges = 3
    num_bananas = 2

    # Calculate the total cost of the fruits
    total_cost = (apple_price * num_apples) + (orange_price * num_oranges) + (banana_price * num_bananas)

    # Calculate the number of fruits Mary bought
    total_fruits = num_apples + num_oranges + num_bananas

    # Calculate the discount Mary will receive for the number of fruits she bought
    discount = (total_fruits // 5) * 1

    # Calculate the final cost after discount
    final_cost = total_cost - discount

    # Return the final cost
    result = final_cost
    return result

print(solution())