def solution():
    """Seven parrots and some crows are perched on a tree branch. There was a noise and the same number of parrots and crows flew away. If only 2 parrots and 1 crow are left on the tree branch now, how many birds were perched on the branch to begin with?"""
    initial_parrots = 9 # 7 + 2 remaining
    initial_crows = 4 # 2 + 2 flew away and 1 remaining
    initial_birds = initial_parrots + initial_crows
    result = initial_birds
    return result

print(solution())