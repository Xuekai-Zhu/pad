def solution():
    popcorn_sales = 50
    cotton_candy_sales = 3 * popcorn_sales
    num_days = 5
    rent = 30
    ingredient_cost = 75

    # Calculate the total sales for popcorn for 5 days
    total_popcorn_sales = popcorn_sales * num_days

    # Calculate the total sales for cotton candy for 5 days
    total_cotton_candy_sales = cotton_candy_sales * num_days

    # Calculate the total earnings for 5 days
    total_earnings = total_popcorn_sales + total_cotton_candy_sales - rent - ingredient_cost
    result = total_earnings
    return result

print(solution())