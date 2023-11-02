def solution():
    hoodie_price = 80
    flashlight_price = hoodie_price * 0.2
    boots_price = 110 * 0.9  # 10% discount

    # Calculate the total cost of all items
    total_cost = hoodie_price + flashlight_price + boots_price
    result = total_cost
    return result

print(solution())