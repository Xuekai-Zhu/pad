def solution():
    """Wendy is a fruit vendor, and she sells an apple at $1.50 each and one orange at $1. In the morning, she was able to sell an average of 40 apples and 30 oranges. In the afternoon, she was able to sell 50 apples and 40 oranges. How much are her total sales for the day?"""
    # Define the price of an apple and an orange
    APPLE_PRICE = 1.5
    ORANGE_PRICE = 1

    # Calculate the total number of apples sold
    total_apples = 40 + 50

    # Calculate the total number of oranges sold
    total_oranges = 30 + 40

    # Calculate the total sales from apples and oranges
    total_sales = (total_apples * APPLE_PRICE) + (total_oranges * ORANGE_PRICE)

    # return the result
    result = total_sales
    return result

print(solution())