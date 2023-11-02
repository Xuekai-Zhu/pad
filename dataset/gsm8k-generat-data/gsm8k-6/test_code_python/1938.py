def solution():
    # Calculate the cost of math and science books
    cost_math_science = 2 * 3 + 6 * 3  # 2 math books and 6 science books cost $3 each

    # Calculate the total cost
    total_cost = 30

    # Calculate the cost of art books
    cost_art = (total_cost - cost_math_science) / 3

    result = cost_art
    return result

print(solution())