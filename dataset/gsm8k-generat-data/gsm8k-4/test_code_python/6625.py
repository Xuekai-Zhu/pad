def solution():
    """Ivan buys 48 apples to make 24 full-size pies. He ends up not using as many as he thought because he decides to make mini pies instead of full-size ones, which only use 1/2 an apple each. If Ivan bakes 24 mini pies, how many apples does he have leftover?"""
    # Calculate the total number of apples needed for the full-size pies
    full_size_apples = 48

    # Calculate the number of apples needed for one full-size pie
    apples_per_pie = full_size_apples / 24

    # Calculate the number of apples needed for one mini pie
    mini_apples_per_pie = 0.5

    # Calculate the total number of apples needed for the mini pies
    mini_pie_apples = mini_apples_per_pie * 24

    # Calculate the number of leftover apples
    leftover_apples = full_size_apples - mini_pie_apples

    # Return the result
    result = leftover_apples
    return result

print(solution())