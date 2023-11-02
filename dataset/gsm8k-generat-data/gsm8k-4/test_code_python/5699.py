def solution():
    """Yanna bought 60 apples. She gave eighteen apples to Zenny. She gave six more apples to Andrea and kept the rest. How many apples did she keep?"""
    # Define the initial number of apples
    initial_apples = 60

    # Subtract the number of apples given to Zenny
    apples_after_zenny = initial_apples - 18

    # Subtract the number of apples given to Andrea
    apples_after_andrea = apples_after_zenny - 6

    # The number of apples Yanna kept
    apples_kept = apples_after_andrea

    # return the result
    result = apples_kept
    return result

print(solution())