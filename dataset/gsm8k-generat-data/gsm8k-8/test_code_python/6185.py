def solution():
    # Calculate the number of coolers produced per hour
    coolers_per_hour = 90 + 70

    # Calculate the total number of products produced per hour
    products_per_hour = 90 + coolers_per_hour

    # Calculate the total number of products produced in 5 days
    total_products = products_per_hour * 9 * 5

    result = total_products
    return result

print(solution())