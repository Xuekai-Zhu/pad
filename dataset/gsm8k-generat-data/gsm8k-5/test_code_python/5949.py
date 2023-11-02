def solution():
    # Initial delivery
    initial_delivery = 50 * 20

    # 20 cartons less delivery
    offloaded_delivery = (50 - 20) * 20

    # Damaged jars and cartons
    damaged_jars = 3 * 5
    damaged_cartons = 1

    # Total damaged milk
    total_damaged = (damaged_jars + (damaged_cartons * 20))

    # Good milk for sale
    good_milk = initial_delivery - offloaded_delivery - total_damaged
    result = good_milk
    return result

print(solution())