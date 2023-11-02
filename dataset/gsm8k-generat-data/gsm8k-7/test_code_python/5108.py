def solution():
    num_fries_packs = 2
    fries_price_per_pack = 2

    salad_price = 3 * fries_price_per_pack

    total_paid = 15

    # Calculate the total cost of the fries
    total_fries_cost = num_fries_packs * fries_price_per_pack

    # Calculate the total cost of the salad
    total_salad_cost = salad_price

    # Calculate the cost of the burger
    burger_cost = total_paid - total_fries_cost - total_salad_cost
    result = burger_cost
    return result

print(solution())