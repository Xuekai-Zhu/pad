def solution():
    initial_production_time = 6
    final_production_time = 5
    difference_in_time = final_production_time - initial_production_time
    additional_pots_per_hour = 60 / difference_in_time
    result = additional_pots_per_hour
    return result

print(solution())