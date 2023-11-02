def solution():
    initial_swans = 15
    growth_factor = 2
    num_years = 10

    # Calculate the number of doublings that will occur in ten years
    num_doublings = num_years // 2

    # Calculate the final number of swans
    final_swans = initial_swans * (growth_factor ** num_doublings)
    result = final_swans
    return result

print(solution())