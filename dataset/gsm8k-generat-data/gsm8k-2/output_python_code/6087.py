def solution():
    """Kim has 4 dozen shirts. She lets her sister have 1/3 of them. How many shirts does she have left?"""
    kim_shirts = 4 * 12
    sister_shirts = kim_shirts / 3
    remaining_shirts = kim_shirts - sister_shirts
    result = remaining_shirts
    return result

print(solution())