def solution():
    num_people = 6  # Zoe and her 5 family members
    num_sodas = num_people  # One soda per person
    soda_price = 0.5

    num_pizzas = num_people  # One slice of pizza per person
    pizza_price = 1.0

    # Calculate the cost of all sodas
    total_soda_cost = num_sodas * soda_price

    # Calculate the cost of all pizzas
    total_pizza_cost = num_pizzas * pizza_price

    # Calculate the total cost of all items
    total_cost = total_soda_cost + total_pizza_cost

    # Zoe takes enough money to pay for the purchase
    amount_taken = total_cost
    result = amount_taken
    return result

print(solution())