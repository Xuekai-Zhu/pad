def solution():
    num_mangoes = 400

    # Calculate the number of ripe mangoes on the tree
    ripe_mangoes = 0.6 * (3/5) * num_mangoes

    # Calculate the number of mangoes Lindsay eats
    lindsay_eats = 0.6 * ripe_mangoes

    # Calculate the number of ripe mangoes remaining
    remaining_mangoes = ripe_mangoes - lindsay_eats
    result = remaining_mangoes
    return result

print(solution())