def solution():
    """Lily is going abroad on vacation with her family. Each of her 4 siblings is bringing 2 suitcases, and her parents are bringing 3 suitcases. Lily decides that there is already too much luggage and she won't be bringing any. How many suitcases is the entire family bringing on vacation?"""
    siblings = 4
    siblings_suitcases = 2
    parents = 2
    parents_suitcases = 3
    total_suitcases = (siblings * siblings_suitcases) + (parents * parents_suitcases)
    result = total_suitcases
    return result

print(solution())