def solution():
    """Ivan buys 48 apples to make 24 full-size pies. He ends up not using as many as he thought because he decides to make mini pies instead of full-size ones, which only use 1/2 an apple each. If Ivan bakes 24 mini pies, how many apples does he have leftover?"""
    full_size_apples_per_pie = 2
    mini_apples_per_pie = 0.5
    total_full_size_apples = full_size_apples_per_pie * 24
    total_mini_apples = mini_apples_per_pie * 24
    total_used_apples = total_full_size_apples + total_mini_apples
    leftover_apples = 48 - total_used_apples
    result = leftover_apples
    return result

print(solution())