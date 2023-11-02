def solution():
    total_weight = 120  # Sandra has a box of apples that weighs 120 pounds
    applesauce_weight = total_weight / 2  # Sandra will use half the weight to make applesauce
    pie_weight = total_weight - applesauce_weight  # Sandra will use the rest to make apple pies

    # Calculate the number of pies Sandra can make
    pies = pie_weight / 4  # Sandra needs 4 pounds of apples per pie

    result = pies
    return result

print(solution())