def solution():
    """3/5 of the mangoes on a mango tree are ripe. If Lindsay eats 60% of the ripe mangoes, calculate the number of ripe mangoes remaining if there were 400 mangoes on the tree to start with."""
    # Define the total number of mangoes
    total_mangoes = 400

    # Calculate the number of ripe mangoes on the tree
    ripe_mangoes = total_mangoes * 3 / 5

    # Calculate the number of ripe mangoes that Lindsay eats
    lindsay_mangoes = ripe_mangoes * 0.6

    # Calculate the number of ripe mangoes remaining on the tree
    remaining_mangoes = ripe_mangoes - lindsay_mangoes

    result = remaining_mangoes
    return result

print(solution())