def solution():
    
    single_layer_price = 4
    double_layer_price = 7
    num_single_layer_slices = 7
    num_double_layer_slices = 5
    total_cost = single_layer_price * num_single_layer_slices + double_layer_price * num_double_layer_slices
    change = 100 - total_cost
    result = change
    return result

print(solution())