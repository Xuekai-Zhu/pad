def solution():
    # Calculate the number of cupcakes made by Betty in 5 hours (excluding her 2-hour break)
    betty_cupcakes = 10 * 3  # Betty makes 10 cupcakes per hour for 3 hours

    # Calculate the number of cupcakes made by Dora in 5 hours
    dora_cupcakes = 8 * 5  # Dora makes 8 cupcakes per hour for 5 hours

    # Calculate the difference between the number of cupcakes made by Betty and Dora
    difference_cupcakes = betty_cupcakes - dora_cupcakes
    result = difference_cupcakes
    return result

print(solution())