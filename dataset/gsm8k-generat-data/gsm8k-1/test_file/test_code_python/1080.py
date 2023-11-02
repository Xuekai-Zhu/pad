def solution():
    """If Sam and Harry have 100 feet of fence between them, and they agree to split it with Harry getting 60 feet more than Sam, how much is left over for Sam?"""
    total_fence = 100
    harry_fence = (total_fence/2)+60
    sam_fence = total_fence/2
    left_over_fence = sam_fence - sam_fence
    result = left_over_fence
    
    return result

print(solution())