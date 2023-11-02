def solution():
    
    packets_of_milk = 150
    ml_per_packet = 250
    ml_to_oz_conversion = 30
    total_ml = packets_of_milk * ml_per_packet
    total_oz = total_ml / ml_to_oz_conversion
    result = total_oz
    
    return result

print(solution())