def solution():
    num_pizzas = 4
    pizza_price = 10

    tip = 5
    total_paid = (num_pizzas * pizza_price) + tip

    amount_given = 50
    change = amount_given - total_paid
    result = change
    return result

print(solution())