def solution():
    # Calculate the number of pairs of plugs in the box before Gunner adds 30 more pairs
    mittens_pairs = 150
    plugs_pairs = mittens_pairs + 20  # box of mittens has 20 fewer pairs than box of plugs
    plugs_pairs_after_addition = plugs_pairs + 30  # Gunner adds 30 more pairs of plugs
    result = plugs_pairs_after_addition
    return result

print(solution())