def solution():
    initial_pairs = 40  # Caroline starts with 40 pairs of socks
    lost_pairs = 4  # She loses 4 pairs at the laundromat
    remaining_pairs = initial_pairs - lost_pairs  # Calculate the number of remaining pairs of socks
    donated_pairs = (2/3) * remaining_pairs  # Calculate the number of pairs donated to the thrift store
    remaining_pairs -= donated_pairs  # Update the number of remaining pairs after donation
    purchased_pairs = 10  # Caroline purchases 10 new pairs of socks
    gifted_pairs = 3  # Caroline receives 3 pairs of socks as a gift
    total_pairs = remaining_pairs + purchased_pairs + gifted_pairs  # Calculate the total number of pairs of socks
    result = total_pairs
    return result

print(solution())