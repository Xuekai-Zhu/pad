def solution():
    num_layer_cakes = 3
    num_dozen_cupcakes = 6
    num_single_cakes = 12
    num_brownie_pans = 18

    # Calculate the total number of cans of frosting needed
    total_cans = num_layer_cakes + (num_dozen_cupcakes / 2) + (num_single_cakes / 2) + (num_brownie_pans / 2)

    result = total_cans
    return result

print(solution())