def solution():
    num_meals_8 = 10
    price_meal_8 = 8
    num_meals_10 = 5
    price_meal_10 = 10
    num_meals_4 = 20
    price_meal_4 = 4

    # Calculate the total sales from meals priced at $8 each
    sales_8 = num_meals_8 * price_meal_8

    # Calculate the total sales from meals priced at $10 each
    sales_10 = num_meals_10 * price_meal_10

    # Calculate the total sales from meals priced at $4 each
    sales_4 = num_meals_4 * price_meal_4

    # Calculate the total sales for the day
    total_sales = sales_8 + sales_10 + sales_4
    result = total_sales
    return result

print(solution())