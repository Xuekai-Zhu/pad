def solution():
    """Peter carried $500 to the market.  He bought 6 kilos of potatoes for $2 per kilo, 9 kilos of tomato for $3 per kilo, 5 kilos of cucumbers for $4 per kilo, and 3 kilos of bananas for $5 per kilo.  How much is Peter’s remaining money?"""
    # Define the prices per kilo of each item
    POTATO_PRICE = 2
    TOMATO_PRICE = 3
    CUCUMBER_PRICE = 4
    BANANA_PRICE = 5

    # Define the amount purchased of each item
    potato_amount = 6
    tomato_amount = 9
    cucumber_amount = 5
    banana_amount = 3

    # Calculate the total cost of each item
    potato_cost = potato_amount * POTATO_PRICE
    tomato_cost = tomato_amount * TOMATO_PRICE
    cucumber_cost = cucumber_amount * CUCUMBER_PRICE
    banana_cost = banana_amount * BANANA_PRICE

    # Calculate the total cost of all items
    total_cost = potato_cost + tomato_cost + cucumber_cost + banana_cost

    # Calculate the remaining money
    remaining_money = 500 - total_cost

    # Display the remaining money
    result = remaining_money
    return result

print(solution())