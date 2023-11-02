def solution():
    
    total_promised = 400
    total_received = 285
    sally_carl_share = (total_promised - total_received - 30 - (0.5*30))/2
    result = sally_carl_share
    return result

print(solution())