def solution():
    initial_marbles = 25  # Baez starts with 25 marbles
    lost_marbles = 0.2 * initial_marbles  # Baez loses 20% of her marbles
    marbles_after_loss = initial_marbles - lost_marbles  # Baez has this many marbles after losing 20%
    marbles_after_gift = marbles_after_loss * 2  # Baez receives double the amount she has after losing marbles
    final_marbles = marbles_after_gift  # Baez ends up with this many marbles
    result = final_marbles
    return result

print(solution())