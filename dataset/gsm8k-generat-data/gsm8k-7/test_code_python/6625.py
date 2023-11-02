def solution():
    num_full_size_pies = 24
    num_apples_per_full_size_pie = 2

    num_mini_pies = 24
    num_apples_per_mini_pie = 0.5

    total_apples_used = num_full_size_pies * num_apples_per_full_size_pie
    total_apples_needed_for_mini_pies = num_mini_pies * num_apples_per_mini_pie

    # Calculate the number of leftover apples
    num_leftover_apples = total_apples_used - total_apples_needed_for_mini_pies
    result = num_leftover_apples
    return result

print(solution())