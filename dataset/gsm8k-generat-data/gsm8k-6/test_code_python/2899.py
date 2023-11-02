def solution():
    # Let's assume Mark started with x amount of money.
    # After spending one-half, he had (1/2)x left and spent $14 more.
    # So, his remaining money is (1/2)x - $14.
    # After spending one-third of his starting money, he had (2/3)x left and spent $16 more.
    # So, his remaining money is (2/3)x - $16.
    # Since he had no money left, we can set the equation: (2/3)x - $16 = 0
    # Solving for x, we get x = $24.
    # Therefore, Mark had $24 when he entered the first store.

    starting_money = 24
    result = starting_money
    return result

print(solution())