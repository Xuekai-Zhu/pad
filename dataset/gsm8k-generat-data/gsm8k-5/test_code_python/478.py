def solution():
    # Calculate Steve's weight
    steve_weight = 110 - 8  # Steve is eight pounds lighter than Jim

    # Calculate Stan's weight
    stan_weight = steve_weight + 5  # Stan weighs 5 more pounds than Steve

    # Calculate the total weight of all three of them
    total_weight = jim_weight + steve_weight + stan_weight
    result = total_weight
    return result

print(solution())