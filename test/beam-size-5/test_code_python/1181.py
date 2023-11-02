def solution():
    cheese_pizza_slices = 12
    pepperoni_pizza_slices = 8
    num_friends = 6
    num_cheese_slices_per_friend = 6
    num_pepperoni_slices_per_friend = 4

    # Calculate the total number of cheese pizza slices needed
    total_cheese_slices = num_friends * num_cheese_slices_per_friend

    # Calculate the total number of pepperoni pizza slices needed
    total_pepperoni_slices = num_pepperoni_pizza_slices / pepperoni_slices_per_friend

    # Calculate the total number of pies needed
    total_pies = total_cheese_slices + total_pepperoni_slices
    result = total_pies
    return result

print(solution())