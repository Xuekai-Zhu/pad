def solution():
    """Gunner has a box of mittens with 20 fewer pairs than a box of plugs. He decides to put 30 more pairs of plugs into the box of plugs. If the box of mittens has 150 pairs of mittens, how many plugs are there?"""
    # Define the number of pairs of mittens and the difference in pairs between the boxes
    mittens = 150
    difference = 20

    # Calculate the number of pairs of plugs in the original box
    plugs_orig = mittens + difference

    # Calculate the number of pairs of plugs in the box after adding 30 more pairs
    plugs_new = plugs_orig + 30

    # Display the number of pairs of plugs
    result = plugs_new
    return result

print(solution())