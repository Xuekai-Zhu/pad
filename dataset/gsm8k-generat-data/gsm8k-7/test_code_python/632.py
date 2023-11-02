def solution():
    num_bom_seeds = 300

    # Calculate Gwi's number of seeds
    num_gwi_seeds = num_bom_seeds + 40

    # Calculate Yeon's number of seeds
    num_yeon_seeds = num_gwi_seeds * 3

    # Calculate the total number of seeds
    total_seeds = num_bom_seeds + num_gwi_seeds + num_yeon_seeds
    result = total_seeds
    return result

print(solution())