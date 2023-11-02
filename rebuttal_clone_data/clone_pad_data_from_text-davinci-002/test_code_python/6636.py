def solution():
     original_seeds = 1
     good_soil_seeds = original_seeds / 2
     germinated_seeds = good_soil_seeds / 2
     
     total_seeds = original_seeds + good_soil_seeds + germinated_seeds
     
     return total_seeds

print(solution())