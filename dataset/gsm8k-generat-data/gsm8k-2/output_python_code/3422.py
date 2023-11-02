def solution():
    """There are 14 chickens in the coop, and twice that many in the run. There is 4 less than double the number of chickens free ranging as in the run. How many chickens are free ranging?"""
    coop_chickens = 14
    run_chickens = coop_chickens * 2
    free_ranging_chickens = (2 * run_chickens) - 4
    result = free_ranging_chickens
    return result

print(solution())