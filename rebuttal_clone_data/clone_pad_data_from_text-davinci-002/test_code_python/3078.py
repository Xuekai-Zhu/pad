def solution():
     barbi_weight_lost_per_month = 1.5
     barbi_weight_lost_per_year = barbi_weight_lost_per_month * 12
     luca_weight_lost_per_year = 9
     total_weight_lost_by_luca = luca_weight_lost_per_year * 11
     weight_difference = total_weight_lost_by_luca - barbi_weight_lost_per_year
     result = weight_difference
     return result

print(solution())