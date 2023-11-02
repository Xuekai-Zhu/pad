def solution():
    """Gunner has a box of mittens with 20 fewer pairs than a box of plugs. He decides to put 30 more pairs of plugs into the box of plugs. If the box of mittens has 150 pairs of mittens, how many plugs are there?"""
    mittens = 150
    plugs = mittens + 20
    plugs += 30
    result = plugs
    return result

print(solution())