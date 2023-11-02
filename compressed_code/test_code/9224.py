def solution():
    
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