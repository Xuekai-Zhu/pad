def solution():
    """Seven parrots and some crows are perched on a tree branch. There was a noise and the same number of parrots and crows flew away. If only 2 parrots and 1 crow are left on the tree branch now, how many birds were perched on the branch to begin with?"""
    initial_parrots = 7
    remaining_parrots = 2
    remaining_crows = 1
    flew_away = initial_parrots - remaining_parrots
    birds_perched_initially = flew_away * 2
    result = initial_parrots + birds_perched_initially
    return result

print(solution())