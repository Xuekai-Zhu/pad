def solution():
    """Seven parrots and some crows are perched on a tree branch. There was a noise and the same number of parrots and crows flew away.
    If only 2 parrots and 1 crow are left on the tree branch now, how many birds were perched on the branch to begin with?"""
    # Let the initial number of parrots be p and the initial number of crows be c
    # We know that p + c = 7 (since there were 7 parrots and some crows to begin with)
    # After some flew away, we know that p - x = 2 (where x is the number of parrots that flew away)
    # and c - x = 1 (where x is the number of crows that flew away)

    # Solving for c in the first equation, we get c = 7 - p
    # Substituting this into the second equation, we get p - x + 7 - p - x = 3
    # Simplifying, we get 2x = 4 or x = 2

    # Substituting this value of x into any of the previous equations, we get p = 4
    # Therefore, the initial number of birds on the branch was 7 + 4 = 11

    result = 11
    return result

print(solution())