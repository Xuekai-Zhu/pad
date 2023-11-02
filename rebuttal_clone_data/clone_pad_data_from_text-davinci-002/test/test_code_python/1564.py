def solution():
     eggplants_per_packet = 14
     sunflowers_per_packet = 10
     packets_bought_eggplants = 4
     packets_bought_sunflowers = 6
     total_eggplants = eggplants_per_packet * packets_bought_eggplants
     total_sunflowers = sunflowers_per_packet * packets_bought_sunflowers
     total_plants = total_eggplants + total_sunflowers
     result = total_plants
     return result

print(solution())