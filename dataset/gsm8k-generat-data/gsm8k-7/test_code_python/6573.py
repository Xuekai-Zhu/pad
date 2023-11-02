def solution():
    start_temp = 60
    heat_temp = 240
    cool_temp = 170
    heat_rate = 5
    cool_rate = 7

    # Calculate the time to heat up the candy mixture
    heat_time = (heat_temp - start_temp) / heat_rate

    # Calculate the time to cool down the candy mixture
    cool_time = (heat_temp - cool_temp) / cool_rate

    # Calculate the total time it will take for the candy to be done
    total_time = heat_time + cool_time
    result = total_time
    return result

print(solution())