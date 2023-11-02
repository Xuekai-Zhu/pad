def solution():
    small_pizza = 8
    large_pizza = 14
    total_slices = small_pizza + large_pizza
    eaten = 9
    left_over = total_slices - eaten
    result = left_over / 2
    return result

print(solution())