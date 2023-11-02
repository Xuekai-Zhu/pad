def solution():
    hot_dog_cost = 1.5  # Each hot dog costs $1.5
    salad_cost = 2.5  # Each salad costs $2.5
    num_hot_dogs = 5  # Ursula bought 5 hot dogs
    num_salads = 3  # Ursula bought 3 salads
    total_cost = (hot_dog_cost * num_hot_dogs) + (salad_cost * num_salads)  # Total cost of her purchase
    amount_paid = 2 * 10  # Ursula paid with 2 $10 bills
    change = amount_paid - total_cost  # Calculate her change

    result = change
    return result

print(solution())