def solution():
    """Tyler weighs 25 pounds more than Sam. Peter weighs half as much as Tyler. If Peter weighs 65 pounds, how much does Sam weigh, in pounds?"""
    peter_weight = 65
    tyler_weight = 2 * peter_weight
    sam_weight = tyler_weight - 25
    result = sam_weight
    return result

print(solution())