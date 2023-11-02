def solution():
     time_between_products = 5
     num_products = 5
     time_to_apply_makeup = 30
     total_time = time_between_products * (num_products - 1) + time_to_apply_makeup
     result = total_time
     return result

print(solution())