def solution():
    num_teeth_tiger_shark = 180
    num_teeth_hammerhead_shark = num_teeth_tiger_shark / 6
    num_teeth_great_white_shark = 2 * (num_teeth_tiger_shark + num_teeth_hammerhead_shark)

    result = num_teeth_great_white_shark
    return result

print(solution())