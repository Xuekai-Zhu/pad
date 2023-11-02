def solution():
    """Ten stalls have 20 cows each. Mr. Sylas buys 40 cows and divides them equally, putting an equal number of the new cows into each of the twenty stalls. How many cows are in 8 of the stalls?"""
    initial_cows = 10 * 20
    new_cows = 40
    total_stalls = 20
    cows_per_stall = (initial_cows + new_cows) / total_stalls
    cows_in_8_stalls = 8 * cows_per_stall
    result = cows_in_8_stalls
    return result

print(solution())