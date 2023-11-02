def solution():
    initial_size = 100
    num_splits = 2

    # Each split reduces the size of the cloth by half
    donated_size = initial_size / (2 ** num_splits)

    # To find how much cloth is donated over both splits, multiply by the number of splits
    total_donated = donated_size * num_splits
    result = total_donated
    return result

print(solution())