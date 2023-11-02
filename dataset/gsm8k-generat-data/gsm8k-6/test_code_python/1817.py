def solution():
    # Calculate the total volume needed to fill all four tires
    total_volume = 2*500 + (500*0.4) + (500*0.7)  # volumes of the four tires
    # Calculate the number of pumps needed to fill the tires
    total_pumps = total_volume / 50
    result = total_pumps
    return result

print(solution())