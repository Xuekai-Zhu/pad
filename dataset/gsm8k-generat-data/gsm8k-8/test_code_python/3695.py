def solution():
    # Define the cost of a single layer cake slice and a double layer cake slice
    single_layer_cost = 4
    double_layer_cost = 7

    # Calculate the total cost of the slice of cakes Dusty purchased
    total_cost = (single_layer_cost * 7) + (double_layer_cost * 5)

    # Calculate the change Dusty receives after paying with a $100 bill
    change = 100 - total_cost
    result = change
    return result

print(solution())