def solution():
    """There are 100 lions in Londolozi at first. If lion cubs are born at the rate of 5 per month and lions die at the rate of 1 per month, how many lions will there be in Londolozi after 1 year?"""
    initial_lions = 100
    cubs_per_month = 5
    deaths_per_month = 1
    
    # calculate the net gain or loss of lions per month
    net_gain_or_loss = cubs_per_month - deaths_per_month
    
    # calculate the total gain or loss of lions over 1 year
    total_net_gain_or_loss = net_gain_or_loss * 12
    
    # calculate the total number of lions after 1 year
    total_lions = initial_lions + total_net_gain_or_loss
    
    result = total_lions
    return result

print(solution())