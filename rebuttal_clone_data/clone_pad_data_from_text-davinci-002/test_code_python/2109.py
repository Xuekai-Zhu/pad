def solution(): 
     volcanoes = 200
     first_explosion = volcanoes * .20
     second_explosion = (volcanoes - first_explosion) * .40
     final_explosion = (volcanoes - first_explosion - second_explosion) * .50
     result = volcanoes - first_explosion - second_explosion - final_explosion
     
     return result

print(solution())