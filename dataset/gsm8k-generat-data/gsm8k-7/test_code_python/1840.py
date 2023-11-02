def solution():
    # Convert 95 cents to nickels
    num_nickels = 95 // 5

    # Ray gives 25 cents to Peter
    num_nickels -= 5

    # Ray gives twice as many cents to Randi as he gave to Peter
    num_nickels -= 2 * 5

    result = num_nickels
    return result

print(solution())