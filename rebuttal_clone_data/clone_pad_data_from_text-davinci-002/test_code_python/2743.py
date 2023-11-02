def solution():
    inventory_size = 2000
    regular_price = 50
    discount = 80
    discount_percent = discount / 100
    sale_price = regular_price * discount_percent
    percent_sold = 90
    items_sold = inventory_size * (percent_sold / 100)
    total_revenue = sale_price * items_sold
    creditors = 15000
    leftover = total_revenue - creditors
    result = leftover
    return result

print(solution())