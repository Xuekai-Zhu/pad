def solution():
     water_drank_on_mon_thur_sat = 9
     water_drank_on_tues_fri_sun = 8
     total_water_drank = (water_drank_on_mon_thur_sat * 3) + (water_drank_on_tues_fri_sun * 3)
     water_drank_on_wednesday = total_water_drank / 7
     result = water_drank_on_wednesday
     return result

print(solution())