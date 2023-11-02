def solution():
    """A restaurant is counting their sales for the day. They sold 10 meals at $8 each, 5 meals at $10 each, and 20 meals at $4 each. In dollars, how much money did the restaurant make throughout the day?"""
    meal1 = 10 * 8
    meal2 = 5 * 10
    meal3 = 20 * 4
    total_sales = meal1 + meal2 + meal3
    result = total_sales
    return result

print(solution())