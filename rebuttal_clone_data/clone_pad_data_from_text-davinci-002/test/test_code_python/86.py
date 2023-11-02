def solution():
     
     mangoes_harvested = 60
     mangoes_sold = 20
     mangoes_left = mangoes_harvested - mangoes_sold
     mangoes_community = mangoes_left / 2
     mangoes_remaining = mangoes_left - mangoes_community
     mangoes_per_kilogram = 8
     result = mangoes_remaining * mangoes_per_kilogram
     return result

print(solution())