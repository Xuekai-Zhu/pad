def solution():
    # Calculate the weight of apples Sandra will use for making applesauce
    applesauce_weight = 120 / 2

    # Calculate the weight of apples Sandra will use for making apple pies
    pie_weight = applesauce_weight - 4  # each pie requires 4 pounds of apples

    # Calculate the number of pies Sandra can make
    num_pies = pie_weight / 4  # each pie requires 4 pounds of apples

    result = num_pies
    return result

print(solution())