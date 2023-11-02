def solution():
    num_piglets = 6
    sale_price = 300
    feeding_cost = 10

    # Calculate the total cost of feeding all piglets until they are fully grown
    total_feeding_cost = num_piglets * feeding_cost * 16

    # Calculate the total revenue from selling all fully grown pigs
    total_revenue = num_piglets * sale_price

    # Calculate the revenue from selling the first 3 pigs after 12 months
    early_sale_revenue = 3 * sale_price

    # Calculate the cost of feeding the first 3 pigs until they are sold
    early_sale_cost = 3 * feeding_cost * 12

    # Calculate the revenue from selling the remaining 3 pigs after 16 months
    late_sale_revenue = 3 * sale_price

    # Calculate the cost of feeding the remaining 3 pigs until they are sold
    late_sale_cost = 3 * feeding_cost * 16

    # Calculate the total profit
    total_profit = total_revenue - total_feeding_cost - early_sale_cost - late_sale_cost + early_sale_revenue + late_sale_revenue

    return total_profit

print(solution())