def solution():
    """Michael saved 5 of his cookies to give Sarah, who saved a third of her 9 cupcakes to give to Michael. How many desserts does Sarah end up with?"""
    # Michael saved 5 cookies for Sarah
    cookies_from_michael = 5

    # Sarah saved a third of her 9 cupcakes to give to Michael
    cupcakes_saved = 9
    cupcakes_given_to_michael = cupcakes_saved / 3

    # Sarah has the remaining desserts after giving cupcakes to Michael
    remaining_desserts = cupcakes_saved - cupcakes_given_to_michael + cookies_from_michael

    # Display the number of desserts Sarah has
    result = remaining_desserts
    return result

print(solution())