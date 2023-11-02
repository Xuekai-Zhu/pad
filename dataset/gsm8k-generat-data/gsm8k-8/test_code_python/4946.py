def solution():
    # Define the number of seeds in bucket A and B
    seeds_in_B = 30
    seeds_in_A = seeds_in_B + 10

    # Calculate the total number of seeds in buckets A and B
    total_seeds_in_A_and_B = seeds_in_A + seeds_in_B

    # Calculate the number of seeds in bucket C
    seeds_in_C = 100 - total_seeds_in_A_and_B

    result = seeds_in_C
    return result

print(solution())