def solution():
    num_sprigs_mint = 3
    num_tea_per_mint = 2

    # Calculate the original number of tea leaves per batch
    original_num_tea = num_sprigs_mint * num_tea_per_mint

    # Calculate the new number of tea leaves per batch
    new_num_tea = original_num_tea * 2

    result = new_num_tea
    return result

print(solution())