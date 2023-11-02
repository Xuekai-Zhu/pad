def solution():
    current_price = 20.00
    tariff_rate = 0.25
    num_bottles = 5

    # Calculate the price increase after tariffs are imposed
    price_increase = current_price * tariff_rate

    # Calculate the new price of one bottle after tariffs are imposed
    new_price = current_price + price_increase

    # Calculate the total cost of 5 bottles of wine after tariffs are imposed
    total_cost = new_price * num_bottles - current_price * num_bottles

    result = total_cost
    return result

print(solution())