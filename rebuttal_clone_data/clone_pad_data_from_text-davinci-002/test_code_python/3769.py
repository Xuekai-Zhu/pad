def solution():
     square_flag = 4*4
     wide_flag = 5*3
     tall_flag = 3*5
     total_square_feet = 1000
     used_square_feet = 16*square_flag + 20*wide_flag + 10*tall_flag
     left_over = total_square_feet - used_square_feet
     result = left_over
     return result

print(solution())