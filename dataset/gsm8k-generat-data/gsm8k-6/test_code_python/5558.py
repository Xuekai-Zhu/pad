def solution():
    # Calculate the total number of parts in the ratio
    total_parts = 5 + 8  # boys : girls = 5:8

    # Calculate the number of parts that represent girls
    girls_parts = 8

    # Calculate the number of girls in the math class
    num_girls = (girls_parts / total_parts) * 260

    result = num_girls
    return result

print(solution())