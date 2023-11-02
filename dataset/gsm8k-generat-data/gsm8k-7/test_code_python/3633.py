def solution():
    bottle_size = 2000  # 2 liters in ml
    sip_size = 40
    num_sips = bottle_size / sip_size
    time_to_drink = num_sips * 5  # 5 minutes per sip
    result = time_to_drink
    return result

print(solution())