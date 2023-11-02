def solution():
    """Joan is at the grocery store. She has a total of $60 to spend. She is going to purchase 2 containers of hummus, which are $5 each. She is going to purchase chicken for $20, bacon for $10, and vegetables for $10. She wants to purchase apples which are $2 each. With her remaining money, how many apples can she purchase?"""
    # Define the prices of each item
    hummus_price = 5
    chicken_price = 20
    bacon_price = 10
    vegetables_price = 10
    apple_price = 2

    # Calculate the total cost of the non-apple items
    total_cost = (2 * hummus_price) + chicken_price + bacon_price + vegetables_price

    # Calculate the remaining money after purchasing the non-apple items
    remaining_money = 60 - total_cost

    # Calculate the maximum number of apples that can be purchased with the remaining money
    max_apples = remaining_money // apple_price

    result = max_apples
    return result

print(solution())