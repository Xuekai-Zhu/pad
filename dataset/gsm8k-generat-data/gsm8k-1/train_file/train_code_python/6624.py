def solution():
    """Ivan buys 48 apples to make 24 full-size pies. He ends up not using as many as he thought because he decides to make mini pies instead of full-size ones, which only use 1/2 an apple each. If Ivan bakes 24 mini pies, how many apples does he have leftover?"""
    full_size_pies = 24
    apples_per_pie = 2
    total_apples = full_size_pies * apples_per_pie
    mini_pies = 24
    apples_per_mini_pie = 0.5
    apples_used = mini_pies * apples_per_mini_pie
    apples_leftover = total_apples - apples_used
    result = apples_leftover
    return result

print(solution())