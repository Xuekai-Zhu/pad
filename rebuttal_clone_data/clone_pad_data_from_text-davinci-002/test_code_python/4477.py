def solution():
    total_batches = 10
    brownies_per_batch = 20
    brownies_reserved = 3/4 * brownies_per_batch
    brownies_in_container = 3/5 * (brownies_per_batch - brownies_reserved)
    brownies_given_out = brownies_per_batch - brownies_reserved - brownies_in_container
    total_brownies_given_out = total_batches * brownies_given_out
    result = total_brownies_given_out
    return result

print(solution())