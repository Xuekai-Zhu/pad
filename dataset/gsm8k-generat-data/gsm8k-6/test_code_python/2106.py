def solution():
    # Calculate the time it took for Emilio to build his house
    emilio_time = 7.5 / 1.5  # since Felipe finished in half the time of Emilio, Emilio took 1.5 times as long as Felipe 
    emilio_months = emilio_time * 12  # convert years to months

    # Calculate the time it took for Felipe to build his house
    felipe_time = emilio_time / 2
    felipe_months = felipe_time * 12  # convert years to months

    result = felipe_months
    return result

print(solution())