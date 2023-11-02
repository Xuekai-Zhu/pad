def solution():

    rate_of_drip = 40
    rate_of_evaporation = 200
    time = 9
    dump = 12000
    
    total_evaporation = rate_of_evaporation * time
    total_drip = rate_of_drip * time
    
    net_loss = total_evaporation + total_drip
    
    result = dump - net_loss
    
    return result

print(solution())