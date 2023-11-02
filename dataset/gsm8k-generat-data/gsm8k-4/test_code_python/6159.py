def solution():
    """A restaurant is counting their sales for the day. They sold 10 meals at $8 each, 5 meals at $10 each, and 20 meals at $4 each. In dollars, how much money did the restaurant make throughout the day?"""
    # Calculate the total sales from each type of meal
    meal1_sales = 10 * 8
    meal2_sales = 5 * 10
    meal3_sales = 20 * 4

    # Calculate the total sales for the day
    total_sales = meal1_sales + meal2_sales + meal3_sales

    # return the result
    result = total_sales
    return result

print(solution())