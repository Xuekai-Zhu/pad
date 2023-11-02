def solution():
    """Dave weighs 175 pounds and can bench press three times his body weight. Craig can only bench press 20% of the amount Dave can. Mark is new and can bench press 50 pounds less than Craig. How much can Mark bench press?"""
    dave_weight = 175
    dave_bench = 3 * dave_weight
    craig_bench = 0.2 * dave_bench
    mark_bench = craig_bench - 50
    result = mark_bench
    return result

print(solution())