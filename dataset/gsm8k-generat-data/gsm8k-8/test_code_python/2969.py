def solution():
    # Calculate the regular price per load of laundry
    regular_price_per_load = 2500 / 80

    # Calculate the sale price per bottle
    sale_price_per_bottle = 2000

    # Calculate the total cost for 2 bottles
    total_cost = 2 * sale_price_per_bottle

    # Calculate the price per load with the sale
    price_per_load_with_sale = total_cost / 80

    result = int(price_per_load_with_sale)
    return result

print(solution())