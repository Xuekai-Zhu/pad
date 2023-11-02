def solution():
    """3/5 of the mangoes on a mango tree are ripe. If Lindsay eats 60% of the ripe mangoes, calculate the number of ripe mangoes remaining if there were 400 mangoes on the tree to start with."""
    # Calculate the number of ripe mangoes on the tree
    ripe_mangoes = 3/5 * 400

    # Calculate the number of ripe mangoes Lindsay eats
    lindsay_eats = 0.6 * ripe_mangoes

    # Calculate the number of ripe mangoes remaining
    remaining_mangoes = ripe_mangoes - lindsay_eats

    # Display the number of ripe mangoes remaining
    result = remaining_mangoes
    return result

print(solution())