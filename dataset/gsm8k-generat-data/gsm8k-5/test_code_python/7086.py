def solution():
    popcorn_sales = 50 * 5  # The booth made $50 selling popcorn each day for 5 days
    cotton_candy_sales = 3 * popcorn_sales  # The booth made three times as much selling cotton candy
    total_sales = popcorn_sales + cotton_candy_sales  # The total sales for 5 days
    total_cost = 30 + 75  # The rent and cost of ingredients for 5 days
    earnings = total_sales - total_cost  # The earnings for 5 days after paying rent and cost of ingredients
    result = earnings
    return result

print(solution())