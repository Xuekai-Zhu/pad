def solution():
    """Wendy is a fruit vendor, and she sells an apple at $1.50 each and one orange at $1.  In the morning, she was able to sell an average of 40 apples and 30 oranges. In the afternoon, she was able to sell 50 apples and 40 oranges. How much are her total sales for the day?"""
    # Define the prices for an apple and an orange
    APPLE_PRICE = 1.50
    ORANGE_PRICE = 1.00

    # Define the number of apples and oranges sold in the morning and afternoon
    morning_apples = 40
    morning_oranges = 30
    afternoon_apples = 50
    afternoon_oranges = 40

    # Calculate the sales for the morning
    morning_sales = (morning_apples * APPLE_PRICE) + (morning_oranges * ORANGE_PRICE)

    # Calculate the sales for the afternoon
    afternoon_sales =(afternoon_apples * APPLE_PRICE) + (afternoon_oranges * ORANGE_PRICE)

    # Calculate the total sales for the day
    total_sales = morning_sales + afternoon_sales

    # Display the total sales for the day
    result = total_sales
    return result

print(solution())