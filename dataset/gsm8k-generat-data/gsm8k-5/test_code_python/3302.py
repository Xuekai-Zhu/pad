def solution():
    mittens_pairs = 150  # Box of mittens has 150 pairs
    plugs_pairs = mittens_pairs + 20  # Box of plugs has 20 more pairs than box of mittens
    updated_plugs_pairs = plugs_pairs + 30  # Gunner adds 30 more pairs of plugs

    # Calculate the total number of plugs
    total_plugs = updated_plugs_pairs * 2  # Each pair contains 2 plugs
    result = total_plugs
    return result

print(solution())