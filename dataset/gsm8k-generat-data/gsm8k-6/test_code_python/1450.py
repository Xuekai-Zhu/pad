def solution():
    # Calculate the number of pairs of socks remaining after losing 4 pairs
    remaining_pairs = 40 - 4

    # Calculate the number of pairs of socks donated to the thrift store
    donated_pairs = (2/3) * remaining_pairs

    # Calculate the total number of pairs of socks Caroline has after donating and purchasing new socks
    total_pairs = remaining_pairs - donated_pairs + 10 + 3

    result = total_pairs
    return result

print(solution())