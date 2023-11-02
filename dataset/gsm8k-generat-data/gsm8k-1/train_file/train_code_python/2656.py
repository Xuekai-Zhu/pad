def solution():
    """A box holds 2 dozen doughnuts. If the family ate 8 doughnuts, how many doughnuts are left?"""
    doughnuts_per_dozen = 12
    doughnuts_per_box = 2 * doughnuts_per_dozen
    doughnuts_eaten = 8
    doughnuts_left = doughnuts_per_box - doughnuts_eaten
    result = doughnuts_left
    return result

print(solution())