def solution():
    # Calculate the total amount of money Jimmy made for the pizzas

    # For the pizzas delivered to the park (less than 1km), delivery charge is not added
    price_park = 3 * 12

    # For the pizzas delivered to the building (more than 1km), delivery charge of 2 dollars is added
    price_building = 2 * (12 + 2)  # 2 pizzas with delivery charge

    # Total amount of money made by Jimmy
    total_money = price_park + price_building
    result = total_money
    return result

print(solution())