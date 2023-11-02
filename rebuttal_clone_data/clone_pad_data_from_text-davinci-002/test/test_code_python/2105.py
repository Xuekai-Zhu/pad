def solution():
    initial_backpack_price = 50
    initial_ring_binder_price = 20
    increased_backpack_price = initial_backpack_price + 5
    reduced_ring_binder_price = initial_ring_binder_price - 2
    total_price = (increased_backpack_price + (reduced_ring_binder_price * 3))
    result = total_price
    return result

print(solution())