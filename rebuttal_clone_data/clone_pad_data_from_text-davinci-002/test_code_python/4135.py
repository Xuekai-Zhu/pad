def solution():
    total_teeth = 32
    teeth_removed_1 = total_teeth * (1/4)
    teeth_removed_2 = total_teeth * (3/8)
    teeth_removed_3 = total_teeth * (1/2)
    teeth_removed_4 = 4
    total_teeth_removed = teeth_removed_1 + teeth_removed_2 + teeth_removed_3 + teeth_removed_4
    result = total_teeth_removed
    return result

print(solution())