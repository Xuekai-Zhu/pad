def solution():
    
    packets_of_milk = 150
    ml_per_packet = 250
    ml_total = packets_of_milk * ml_per_packet
    ounces_total = ml_total / 30
    result = ounces_total
    return result

print(solution())