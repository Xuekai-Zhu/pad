def solution():
    num_adults = 4
    num_children = 8
    num_chocolate_bars_per_packet = 5
    num_chocolate_bars_per_adult = 6
    num_chocolate_bars_per_child = (num_chocolate_bars_per_packet - num_adults * num_chocolate_bars_per_adult) / num_children
    result = num_children
    return result

print(solution())