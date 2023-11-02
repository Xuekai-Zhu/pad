def solution():
    """Gunner has a box of mittens with 20 fewer pairs than a box of plugs. He decides to put 30 more pairs of plugs into the box of plugs. If the box of mittens has 150 pairs of mittens, how many plugs are there?"""
    pairs_of_mittens = 150
    pairs_of_mittens_box = pairs_of_mittens / 2
    pairs_of_plugs_box = pairs_of_mittens_box + 20
    pairs_of_plugs_box += 30
    pairs_of_plugs = pairs_of_plugs_box * 2
    
    result = pairs_of_plugs
    
    return result

print(solution())