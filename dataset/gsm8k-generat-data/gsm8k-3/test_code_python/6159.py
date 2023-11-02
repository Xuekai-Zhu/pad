def solution():
    """A restaurant is counting their sales for the day. They sold 10 meals at $8 each, 5 meals at $10 each, and 20 meals at $4 each. In dollars, how much money did the restaurant make throughout the day?"""
    # Define the number of each type of meal sold and their prices
    MEAL1_NUM = 10
    MEAL1_PRICE = 8
    MEAL2_NUM = 5
    MEAL2_PRICE = 10
    MEAL3_NUM = 20
    MEAL3_PRICE = 4

    # Calculate the total sales for each type of meal
    meal1_sales = MEAL1_NUM * MEAL1_PRICE
    meal2_sales = MEAL2_NUM * MEAL2_PRICE
    meal3_sales = MEAL3_NUM * MEAL3_PRICE

    # Calculate the total sales for the day
    total_sales = meal1_sales + meal2_sales + meal3_sales

    # Display the total sales
    result = total_sales
    return result

print(solution())