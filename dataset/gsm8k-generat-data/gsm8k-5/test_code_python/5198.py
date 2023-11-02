def solution():
    pairs_bought = 12  # Lisa bought 12 pairs of socks
    pairs_from_friend = 20  # Sandra brought 20 pairs of socks
    pairs_from_cousin = pairs_from_friend / 5  # Lisa's cousin brought one-fifth the number of pairs that Sandra bought
    pairs_from_mom = 8 + (3 * pairs_bought)  # Lisa's mom brought 8 more than three times the number of pairs Lisa started with

    # Calculate the total number of pairs of socks Lisa ends up with
    total_pairs = pairs_bought + pairs_from_friend + pairs_from_cousin + pairs_from_mom
    result = total_pairs
    return result

print(solution())