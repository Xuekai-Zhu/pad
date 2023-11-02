def solution():
    burger_price = 5
    sandwich_price = 4
    smoothie_price = 4
    num_smoothies = 2

    # Calculate the total cost of the fast-food order
    total_cost = burger_price + sandwich_price + (smoothie_price * num_smoothies)
    result = total_cost
    return result

print(solution())