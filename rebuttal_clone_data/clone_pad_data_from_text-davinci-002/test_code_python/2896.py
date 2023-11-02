def solution():
     log_length = 20
     log_weight = 150
     log_weight_per_foot = log_weight / log_length
     half_log_length = log_length / 2
     half_log_weight = half_log_length * log_weight_per_foot
     result = half_log_weight
     return result

print(solution())