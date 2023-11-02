def solution():
     initial_green_leaves = 18
     leaves_that_turn_yellow = initial_green_leaves / 3
     leaves_that_fall_off = leaves_that_turn_yellow
     total_green_leaves_left = initial_green_leaves - leaves_that_fall_off
     result = total_green_leaves_left
     return result

print(solution())