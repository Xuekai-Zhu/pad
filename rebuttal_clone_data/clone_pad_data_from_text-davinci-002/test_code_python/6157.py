def solution():
    num_disappearances = 100
    fraction_reappeared = 9/10
    num_reappeared = num_disappearances * fraction_reappeared
    fraction_two_reappeared = 1/5
    num_two_reappeared = num_disappearances * fraction_two_reappeared
    total_reappeared = num_reappeared + (2 * num_two_reappeared)
    result = total_reappeared
    return result

print(solution())