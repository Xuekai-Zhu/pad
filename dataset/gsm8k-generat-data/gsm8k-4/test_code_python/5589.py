def solution():
    """Michael saved 5 of his cookies to give Sarah, who saved a third of her 9 cupcakes to give to Michael. How many desserts does Sarah end up with?"""
    # Calculate the number of cupcakes Sarah saved
    cupcakes_saved = 9 * (1/3)

    # Calculate the total number of desserts Sarah ends up with
    total_desserts = cupcakes_saved + 5

    result = total_desserts
    return result

print(solution())