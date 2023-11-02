def solution():
    total_pairs = 1250 # Total pairs of shoes in the warehouse
    blue_pairs = 540 # Number of pairs that are blue
    green_purple_pairs = total_pairs - blue_pairs # Number of pairs that are either green or purple

    # Since the number of green shoes is equal to the number of purple shoes, we can divide the remaining pairs into two equal parts
    purple_pairs = green_purple_pairs / 2
    result = purple_pairs
    return result

print(solution())