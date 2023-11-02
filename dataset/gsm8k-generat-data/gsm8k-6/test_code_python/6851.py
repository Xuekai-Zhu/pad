def solution():
    # Calculate the total cost of the small glasses that Peter bought
    small_cost = 3 * 8

    # Calculate how much Peter spent on large glasses
    spent_on_large = 50 - small_cost - 1

    # Calculate how many large glasses Peter bought
    num_large = spent_on_large // 5

    result = num_large
    return result

print(solution())