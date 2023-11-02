def solution():
    # Define the price of one pack of fries and the price of the salad
    fries_price = 2
    salad_price = fries_price * 3

    # Calculate the total cost of the fries and the salad
    total_food_price = 2 * fries_price + salad_price

    # Calculate the cost of the burger
    burger_price = 15 - total_food_price

    result = burger_price
    return result

print(solution())