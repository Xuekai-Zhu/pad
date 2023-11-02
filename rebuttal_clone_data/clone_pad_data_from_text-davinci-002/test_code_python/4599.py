def solution():
     packets_bought = 150
     ml_per_packet = 250
     ml_per_oz = 30
     total_ml = packets_bought * ml_per_packet
     total_ounces = total_ml / ml_per_oz
     result = total_ounces
     
     return result

print(solution())