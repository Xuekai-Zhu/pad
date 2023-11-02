def solution():
    """Steve bought $25 worth of groceries. He bought a gallon of milk for $3, two boxes of cereal for $3.5 each, 4 bananas for $.25 each, four apples that cost $.5 each and a number of boxes of cookies. The cookies cost twice as much per box as the gallon of milk. How many boxes of cookies did he get?"""
    # Define the prices of each item
    MILK_PRICE = 3
    CEREAL_PRICE = 3.5
    BANANA_PRICE = 0.25
    APPLE_PRICE = 0.5
    COOKIES_PRICE = 2 * MILK_PRICE

    # Define the quantities of each item purchased
    milk_quantity = 1
    cereal_quantity = 2
    banana_quantity = 4
    apple_quantity = 4

    # Calculate the total cost of the first 5 items
    total_cost = (milk_quantity * MILK_PRICE) + (cereal_quantity * CEREAL_PRICE) + (banana_quantity * BANANA_PRICE) + (apple_quantity * APPLE_PRICE)

    # Calculate the cost of the cookies
    cookies_cost = 25 - total_cost

    # Calculate the number of boxes of cookies purchased
    cookies_boxes = cookies_cost / COOKIES_PRICE

    # Display the number of boxes of cookies purchased
    result = cookies_boxes
    return result

print(solution())