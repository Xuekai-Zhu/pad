def solution():
    single_layer_price = 4  # Price per single layer cake slice is $4
    double_layer_price = 7  # Price per double layer cake slice is $7
    num_single_layer = 7  # Dusty buys 7 single layer cake slices
    num_double_layer = 5  # Dusty buys 5 double layer cake slices
    total_price = (single_layer_price * num_single_layer) + (double_layer_price * num_double_layer)  # Calculate total amount spent
    change = 100 - total_price  # Calculate change
    result = change
    return result

print(solution())