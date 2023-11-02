def solution():
    num_packs = 9
    packs_per_pack = 8
    left_over = 40

    # Calculate the total number of candy necklaces that Emily had initially
    total_init_necklaces = num_packs * packs_per_pack

    # Calculate the total number of candy necklaces that Emily's classmates took
    num_taken = total_init_necklaces - left_over

    # Calculate the number of packs that Emily opened for her classmates
    packs_opened = num_taken // packs_per_pack
    result = packs_opened
    return result

print(solution())