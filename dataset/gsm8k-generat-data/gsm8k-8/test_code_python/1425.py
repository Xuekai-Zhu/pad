def solution():
    # Calculate the cupcakes made by Betty in 5 hours
    betty_cupcakes = 10 * 3

    # Calculate the cupcakes made by Dora in 5 hours
    dora_cupcakes = 8 * 5

    # Calculate the cupcakes made by Betty after her break
    betty_cupcakes_after_break = 10 * 2

    # Calculate the total number of cupcakes made by Betty and Dora after 5 hours
    total_cupcakes = betty_cupcakes + dora_cupcakes + betty_cupcakes_after_break

    # Calculate the difference between the cupcakes made by Betty and Dora after 5 hours
    difference = betty_cupcakes_after_break - dora_cupcakes

    result = difference
    return result

print(solution())