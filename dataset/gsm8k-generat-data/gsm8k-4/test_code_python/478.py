def solution():
    """Stan weighs 5 more pounds than Steve. Steve is eight pounds lighter than Jim. If Jim weighs 110 pounds and the three of them crowd onto a scale at the same time, what is their total weight?"""
    # Calculate Steve's weight
    steve_weight = 110 - 8

    # Calculate Stan's weight
    stan_weight = steve_weight + 5

    # Calculate the total weight
    total_weight = jim_weight + steve_weight + stan_weight

    # return the result
    result = total_weight
    return result

print(solution())