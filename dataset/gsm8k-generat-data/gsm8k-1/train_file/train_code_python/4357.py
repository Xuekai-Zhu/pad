def solution():
    """A mother is serving pizza at her son's birthday party. After buying 5 pizzas, she must decide how many slices to divide each pizza into so that everyone at the party ends up with an equal number of slices. There are a total of 20 children at the party, and she can choose to divide each pizza into either 6, 8, or 10 slices. Assuming she does not want to throw away any pizza, how should many slices should she choose to divide the pizzas into to make sure everyone receives an equal amount?"""
    num_pizzas = 5
    num_children = 20
    num_slices = [6, 8, 10]
    equal_slices = None
    for slices in num_slices:
        if num_pizzas * slices % num_children == 0:
            equal_slices = slices
            break
    result = equal_slices
    return result

print(solution())