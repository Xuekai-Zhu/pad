def solution():
    """A box holds 2 dozen doughnuts. If the family ate 8 doughnuts, how many doughnuts are left?"""
    total_doughnuts = 2 * 12
    eaten_doughnuts = 8
    remaining_doughnuts = total_doughnuts - eaten_doughnuts
    result = remaining_doughnuts
    return result

print(solution())