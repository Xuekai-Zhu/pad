def solution():
    # Calculate the total number of cupcakes baked
    total_cupcakes = 4 * 20  # each tray has 20 cupcakes and there are 4 trays

    # Calculate the number of cupcakes sold
    sold_cupcakes = (3/5) * total_cupcakes

    # Calculate the amount earned from sold cupcakes
    earned_amount = sold_cupcakes * 2  # each cupcake was sold for $2

    result = earned_amount
    return result

print(solution())