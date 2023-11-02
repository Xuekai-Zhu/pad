def solution():
    # Define the number of pairs of mittens
    mitten_pairs = 150

    # Calculate the number of pairs of plugs in the original box
    plug_pairs_original = mitten_pairs + 20

    # Add 30 pairs of plugs to the box
    plug_pairs_new = plug_pairs_original + 30

    result = plug_pairs_new
    return result

print(solution())