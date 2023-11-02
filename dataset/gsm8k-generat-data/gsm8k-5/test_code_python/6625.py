def solution():
    apples_per_pie = 2  # Ivan originally planned to use 2 apples per full-size pie
    full_size_pies = 24  # Ivan bought enough apples for 24 full-size pies
    total_apples = apples_per_pie * full_size_pies  # Calculate the total number of apples Ivan bought

    mini_pie_apples = 0.5  # Each mini pie requires 1/2 an apple
    mini_pies = 24  # Ivan ended up making 24 mini pies
    used_apples = mini_pie_apples * mini_pies  # Calculate the number of apples used for the mini pies

    # Calculate the number of leftover apples
    leftover_apples = total_apples - used_apples
    result = leftover_apples
    return result

print(solution())