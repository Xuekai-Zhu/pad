def solution():
    # Define the prices of the items
    toy_car_price = 11
    scarf_price = 10
    beanie_price = 14

    # Calculate the total amount spent on the items
    total_spent = 2 * toy_car_price + scarf_price + beanie_price + 7

    # Calculate the amount of money Sarah started with
    starting_amount = total_spent - 2 * toy_car_price
    result = starting_amount
    return result

print(solution())