def solution():
    
    single_layer_price = 4
    double_layer_price = 7
    single_layer_slices = 7
    double_layer_slices = 5
    total_price = (single_layer_price * single_layer_slices) + (double_layer_price * double_layer_slices)
    change = 100 - total_price
    result = change
    return result

print(solution())