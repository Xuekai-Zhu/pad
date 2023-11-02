def solution():
    # Calculate the total number of popcorn kernels dropped by Jenny
    total_popcorn_dropped = 5000 / 25  # 1 kernel per 25 feet walked

    # Calculate the number of popcorn kernels eaten by the squirrel
    eaten_popcorn = total_popcorn_dropped / 4  # one-quarter of the popcorn was eaten

    # Calculate the remaining popcorn kernels on the ground
    remaining_popcorn = total_popcorn_dropped - eaten_popcorn

    result = remaining_popcorn
    return result

print(solution())