def solution():
    """Yanna bought 60 apples. She gave eighteen apples to Zenny. She gave six more apples to Andrea and kept the rest. How many apples did she keep?"""
    total_apples = 60
    apples_given_zenny = 18
    apples_given_andrea = 6
    apples_kept = total_apples - apples_given_zenny - apples_given_andrea
    result = apples_kept
    return result

print(solution())