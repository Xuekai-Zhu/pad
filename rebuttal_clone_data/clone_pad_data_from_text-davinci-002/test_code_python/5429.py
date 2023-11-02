def solution():
     sticks_per_group = 15
     number_of_groups = 10
     total_sticks = sticks_per_group * number_of_groups
     left_over_sticks = 170 - total_sticks
     result = left_over_sticks
     return result

print(solution())