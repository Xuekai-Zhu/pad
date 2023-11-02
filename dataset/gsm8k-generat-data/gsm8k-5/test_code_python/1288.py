def solution():
    vacuuming_time = 3  # James spends 3 hours vacuuming
    # James spends 3 times as long on the rest of his chores, so the total time spent on chores is:
    total_chore_time = vacuuming_time + (3 * vacuuming_time)
    result = total_chore_time
    return result

print(solution())