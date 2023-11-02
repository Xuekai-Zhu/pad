def solution():
    pizza_price = 12
    fries_price = 0.3
    soda_price = 2
    target_amount = 500

    num_pizzas = 15
    num_fries = 40
    num_sodas = 25

    # Calculate the total amount raised from selling pizzas
    pizza_amount = num_pizzas * pizza_price

    # Calculate the total amount raised from selling fries
    fries_amount = num_fries * fries_price

    # Calculate the total amount raised from selling sodas
    soda_amount = num_sodas * soda_price

    # Calculate the total amount raised from all snack sales
    total_amount = pizza_amount + fries_amount + soda_amount

    # Calculate the difference between the target amount and the total amount raised
    shortfall = target_amount - total_amount
    result = shortfall
    return result

print(solution())