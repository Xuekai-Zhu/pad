def solution():
    """Ivan buys 48 apples to make 24 full-size pies. He ends up not using as many as he thought because he decides to make mini pies instead of full-size ones, which only use 1/2 an apple each. If Ivan bakes 24 mini pies, how many apples does he have leftover?"""
    # Calculate the total number of apples needed for the full-size pies
    full_size_apples = 48
    apples_per_full_size_pie = 2 # Each full-size pie uses 2 apples
    apples_used_for_full_size_pies = 24 * apples_per_full_size_pie

    # Calculate the number of apples used for the mini pies
    apples_used_for_mini_pies = 24 * 0.5 # Each mini pie uses 0.5 apples

    # Calculate the total number of apples used
    total_apples_used = apples_used_for_full_size_pies + apples_used_for_mini_pies

    # Calculate the number of leftover apples
    leftover_apples = full_size_apples - total_apples_used

    # Display the number of leftover apples
    result = leftover_apples
    return result

print(solution())