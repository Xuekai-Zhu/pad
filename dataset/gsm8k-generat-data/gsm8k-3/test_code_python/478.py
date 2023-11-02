def solution():
    """Stan weighs 5 more pounds than Steve. Steve is eight pounds lighter than Jim. If Jim weighs 110 pounds and the three of them crowd onto a scale at the same time, what is their total weight?"""
    # Define Jim's weight
    jim_weight = 110

    # Calculate Steve's weight
    steve_weight = jim_weight - 8

    # Calculate Stan's weight
    stan_weight = steve_weight + 5

    # Calculate the total weight of all three
    total_weight = jim_weight + steve_weight + stan_weight

    # Display the total weight
    result = total_weight
    return result

print(solution())