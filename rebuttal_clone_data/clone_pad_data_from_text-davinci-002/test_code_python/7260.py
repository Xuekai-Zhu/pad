def solution():
     blackbirds_per_tree = 3
     trees_in_park = 7
     magpies_in_park = 13
     total_blackbirds = blackbirds_per_tree * trees_in_park
     total_birds = total_blackbirds + magpies_in_park
     result = total_birds
     return result

print(solution())