def solution():
    max_weight = 50  # limit set by Tony's dad
    pants_weight = 10
    shirt_weight = 5
    shorts_weight = 8
    socks_weight = 2
    underwear_weight = 4

    # Calculate the total weight of Tony's current load
    current_weight = (1 * pants_weight) + (2 * shirt_weight) + (1 * shorts_weight) + (3 * socks_weight)

    # Calculate the remaining weight that Tony can add to the wash
    remaining_weight = max_weight - current_weight

    # Calculate the number of pairs of underwear that can be added to the wash
    num_underwear = remaining_weight / underwear_weight
    result = num_underwear
    return result

print(solution())