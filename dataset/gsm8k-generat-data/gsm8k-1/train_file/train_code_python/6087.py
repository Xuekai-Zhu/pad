def solution():
    """Kim has 4 dozen shirts. She lets her sister have 1/3 of them. How many shirts does she have left?"""
    shirts_per_dozen = 12
    total_shirts = 4 * shirts_per_dozen
    sister_shirts = total_shirts / 3
    remaining_shirts = total_shirts - sister_shirts
    result = remaining_shirts
    return result

print(solution())