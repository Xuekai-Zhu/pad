def solution():
     small_panda_bamboo = 25
     big_panda_bamboo = 40
     small_pandas = 4
     big_pandas = 5
     total_bamboo = (small_panda_bamboo * small_pandas) + (big_panda_bamboo * big_pandas)
     bamboo_per_week = total_bamboo * 7
     result = bamboo_per_week
     return result

print(solution())