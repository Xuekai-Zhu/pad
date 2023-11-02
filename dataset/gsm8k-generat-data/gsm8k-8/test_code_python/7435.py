def solution():
    # Calculate how many maggots were thrown out after the first attempt
    maggots_thrown_out = 10 - 1

    # Calculate how many maggots were left for the second attempt
    maggots_left = 20 - (10 - maggots_thrown_out)

    # Calculate how many maggots were fed the second time
    maggots_fed_second_time = 3

    # Calculate how many maggots were attempted to be fed the second time
    attempted_maggots_second_time = maggots_left - maggots_fed_second_time

    result = attempted_maggots_second_time
    return result

print(solution())