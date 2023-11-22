def solution():
    
    # Define the daily electric consumption and the device consumption
    daily_consumption = 12
    device_consumption = 2

    # Calculate the total electric consumption before and after adding the device
    total_consumption = daily_consumption * 7
    total_consumption += device_consumption * 7

    # Calculate the difference between the two electric bills before and after adding the device
    difference = total_consumption - total_consumption

    # return the result
    result = difference
    return result

print(solution())