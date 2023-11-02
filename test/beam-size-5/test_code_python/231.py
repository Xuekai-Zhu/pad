def solution():
    num_friends = 20
    slices_per_friend = 4
    num_slices_per_pizza = 8

    # Calculate the total number of slices needed
    total_slices = num_friends * slices_per_friend

    # Calculate the number of pizzas needed
    num_pizzas = total_slices // slices_per_pizza
    if total_slices % slices_per_pizza!= 0:
        num_pizzas += 1

    result = num_pizzas
    return result

print(solution())