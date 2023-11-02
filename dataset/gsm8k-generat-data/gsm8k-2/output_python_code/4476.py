def solution():
    """Melanie baked 10 batches of brownies, with 20 brownies in each batch. She set aside 3/4 of the brownies in each batch for a bake sale, put 3/5 of the remaining in a container, and gave out the rest. How many brownies are given out?"""
    total_brownies = 10 * 20
    for_sale_brownies = total_brownies * 3 / 4
    remaining_brownies = total_brownies - for_sale_brownies
    container_brownies = remaining_brownies * 3 / 5
    given_out_brownies = remaining_brownies - container_brownies
    result = given_out_brownies
    return result

print(solution())