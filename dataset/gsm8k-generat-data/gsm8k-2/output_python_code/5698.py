def solution():
    """Yanna bought 60 apples. She gave eighteen apples to Zenny. She gave six more apples to Andrea and kept the rest. How many apples did she keep?"""
    total_apples = 60
    zenny_apples = 18
    andrea_apples = 6
    kept_apples = total_apples - zenny_apples - andrea_apples
    result = kept_apples
    return result

print(solution())