def solution():
    """A mother is serving pizza at her son's birthday party. After buying 5 pizzas, she must decide how many slices to divide each pizza into so that everyone at the party ends up with an equal number of slices. There are a total of 20 children at the party, and she can choose to divide each pizza into either 6, 8, or 10 slices. Assuming she does not want to throw away any pizza, how should many slices should she choose to divide the pizzas into to make sure everyone receives an equal amount?"""
    total_slices = 5 * (6 + 8 + 10)
    num_children = 20
    min_slices_per_child = total_slices // num_children

    # checking which slice options divide evenly
    if min_slices_per_child % 6 == 0:
        num_slices = 6
    elif min_slices_per_child % 8 == 0:
        num_slices = 8
    elif min_slices_per_child % 10 == 0:
        num_slices = 10
    else:
        num_slices = min_slices_per_child

    result = num_slices
    return result

print(solution())