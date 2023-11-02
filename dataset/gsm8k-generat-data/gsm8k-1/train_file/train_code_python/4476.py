def solution():
    """Melanie baked 10 batches of brownies, with 20 brownies in each batch. She set aside 3/4 of the brownies in each batch for a bake sale, put 3/5 of the remaining in a container, and gave out the rest. How many brownies are given out?"""
    batches = 10
    brownies_per_batch = 20
    bake_sale_portion = 3/4
    remaining_portion = 1 - bake_sale_portion
    container_portion = 3/5
    given_out_portion = 1 - container_portion
    brownies_for_sale = batches * brownies_per_batch * bake_sale_portion
    brownies_remaining = batches * brownies_per_batch * remaining_portion
    brownies_in_container = brownies_remaining * container_portion
    brownies_given_out = brownies_remaining * given_out_portion
    result = brownies_given_out
    return result

print(solution())