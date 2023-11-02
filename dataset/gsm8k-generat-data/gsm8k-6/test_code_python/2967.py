def solution():
    # Calculate Dave's bench press weight
    dave_bench = 3 * 175  # Dave can bench press three times his body weight

    # Calculate Craig's bench press weight
    craig_bench = 0.2 * dave_bench  # Craig can only bench press 20% of what Dave can

    # Calculate Mark's bench press weight
    mark_bench = craig_bench - 50  # Mark can bench press 50 pounds less than Craig

    result = mark_bench
    return result

print(solution())