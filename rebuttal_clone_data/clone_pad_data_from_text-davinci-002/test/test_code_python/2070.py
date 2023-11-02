def solution():
    drip_rate = 3 #drops/minute
    drop_size = 20/1000 #ml to liters
    pot_size = 3 #liters
    time_to_fill = (pot_size / drip_rate) / drop_size #minutes
    result = time_to_fill
    return result

print(solution())