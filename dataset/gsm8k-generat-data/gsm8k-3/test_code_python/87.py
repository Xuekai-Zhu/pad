def solution():
    """John's cow weighs 400 pounds. It increased its weight to 1.5 times its starting weight. He is able to sell the cow for $3 per pound. How much more is it worth after gaining the weight?"""
    # Define the initial weight of the cow
    initial_weight = 400

    # Calculate the new weight of the cow after increasing by 1.5 times
    new_weight = 1.5 * initial_weight

    # Calculate the difference in value before and after the weight gain
    value_diff = (new_weight - initial_weight) * 3

    # return the result
    result = value_diff
    return result

print(solution())