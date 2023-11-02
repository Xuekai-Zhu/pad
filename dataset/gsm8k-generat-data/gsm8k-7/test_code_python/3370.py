def solution():
    total_watermelons_sold = 46
    num_customers_1 = 17
    num_customers_3 = 3

    # Calculate the total number of watermelons bought by customers who did not buy 2
    total_watermelons_excl_2 = num_customers_1 + (num_customers_3 * 3)

    # Calculate the total number of customers who bought 2 watermelons
    num_customers_2 = (total_watermelons_sold - total_watermelons_excl_2) / 2

    result = num_customers_2
    return result

print(solution())