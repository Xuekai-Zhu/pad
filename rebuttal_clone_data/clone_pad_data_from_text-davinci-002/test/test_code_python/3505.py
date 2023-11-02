def solution():
    total_grams = 800
    grams_per_large_order = 200
    grams_per_small_order = 50
    large_orders = 3
    small_orders = (total_grams - (large_orders * grams_per_large_order)) / grams_per_small_order
    result = small_orders
    return result

print(solution())