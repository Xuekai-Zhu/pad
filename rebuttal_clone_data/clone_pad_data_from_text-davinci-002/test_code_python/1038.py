def solution():
     seeds_planted = 23
     seeds_not_grown = 5
     seeds_eaten = (seeds_planted - seeds_not_grown) / 3
     remaining_plants = (seeds_planted - seeds_not_grown) - seeds_eaten
     weed_plants_strangled = remaining_plants / 3
     remaining_plants = remaining_plants - weed_plants_strangled
     final_plants = remaining_plants - 2
     result = final_plants
     return result

print(solution())