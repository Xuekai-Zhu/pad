def solution():
    # Calculate the total amount of sugar available
    total_sugar = 3 + 2*6  # 3 cups at home plus 2 bags of 6 cups each

    # Calculate the number of cupcakes that can be made
    cupcakes_per_cup = 12  # 1 cup of sugar makes 12 cupcakes
    cupcakes_without_frosting = total_sugar * cupcakes_per_cup  # total number of cupcakes without frosting
    frosting_sugar_per_dozen = 2  # 2 cups of sugar per dozen cupcakes for frosting
    cupcakes_with_frosting = (total_sugar//frosting_sugar_per_dozen) * cupcakes_per_cup

    result = min(cupcakes_without_frosting, cupcakes_with_frosting) // cupcakes_per_cup
    return result

print(solution())