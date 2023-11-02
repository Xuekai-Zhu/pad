def solution():
    
    initial_lions = 100
    cubs_per_month = 5
    deaths_per_month = 1
    
    
    net_gain_or_loss = cubs_per_month - deaths_per_month
    
    
    total_net_gain_or_loss = net_gain_or_loss * 12
    
    
    total_lions = initial_lions + total_net_gain_or_loss
    
    result = total_lions
    return result

print(solution())