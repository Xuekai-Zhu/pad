def solution():
    """Helen cuts her lawn starting in March and finishes in October.  
    Her lawn mower uses 2 gallons of gas every 4th time she cuts her lawn.  
    For March, April, September and October, she only cuts her law 2 times per month.  
    In May, June, July and August, she has to cut her lawn 4 times per month.  
    How many gallons of gas will she need to cut her lawn from March through October?"""
    
    # Define the number of times she cuts her lawn for each month
    mow_per_month = {'Mar': 2, 'Apr': 2, 'May': 4, 'Jun': 4, 'Jul': 4, 'Aug': 4, 'Sep': 2, 'Oct': 2}

    # Define the number of times she uses 2 gallons of gas
    gas_use_count = 0
    
    # Loop over the months and count the number of times she needs gas
    for month in mow_per_month:
        mows = mow_per_month[month]
        if mows % 4 == 0:
            gas_use_count += mows // 4
    
    # Calculate the total number of gallons of gas needed
    total_gas = 2 * gas_use_count
    
    # Return the result
    return total_gas

print(solution())