def solution():
    # Calculate the number of chickens in the run
    chickens_in_coop = 14
    chickens_in_run = 2 * chickens_in_coop
    # Calculate the number of chickens free ranging
    free_ranging_chickens = (2 * chickens_in_run) - 4
    result = free_ranging_chickens
    return result

print(solution())