def solution():
    acres_bought = 200  # Mike bought 200 acres of land
    price_per_acre = 70  # Mike paid $70 per acre
    total_cost = acres_bought * price_per_acre  # Calculate the total cost of the land

    acres_sold = acres_bought / 2  # Mike sold half of the acreage
    price_per_acre_sold = 200  # Mike sold the land for $200 per acre
    total_revenue = acres_sold * price_per_acre_sold  # Calculate the total revenue from selling the land

    # Calculate the profit Mike made
    profit = total_revenue - total_cost
    result = profit
    return result

print(solution())