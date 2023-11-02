def solution():
    """Gunner has a box of mittens with 20 fewer pairs than a box of plugs. He decides to put 30 more pairs of plugs into the box of plugs. If the box of mittens has 150 pairs of mittens, how many plugs are there?"""
    # Define the initial number of pairs of mittens
    mittens = 150

    # Calculate the number of pairs of plugs in the initial box
    plugs_initial = mittens + 20

    # Calculate the number of pairs of plugs after Gunner adds 30 more pairs
    plugs_final = plugs_initial + 30

    result = plugs_final
    return result

print(solution())