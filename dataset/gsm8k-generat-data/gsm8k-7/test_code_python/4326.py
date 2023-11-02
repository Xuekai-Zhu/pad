def solution():
    num_oranges_L = 40
    price_L = 2.5 / 2  # Liam sold 2 oranges for $2.50
    num_oranges_C = 30
    price_C = 1.2
    total_L = num_oranges_L * price_L
    total_C = num_oranges_C * price_C
    total_saved = total_L + total_C
    result = total_saved
    return result

print(solution())