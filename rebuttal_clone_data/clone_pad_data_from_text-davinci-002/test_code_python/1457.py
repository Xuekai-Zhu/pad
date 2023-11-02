def solution():
     sacks_ rice_field = 20
     percent_increase = 20
     yield_after_first_harvest = sacks_rice_field + (sacks_rice_field * (percent_increase / 100))
     yield_after_second_harvest = yield_after_first_harvest + (yield_after_first_harvest * (percent_increase / 100))
     total_sacks = yield_after_first_harvest + yield_after_second_harvest
     result = total_sacks
     return result

print(solution())