def solution():
    # Define the weight and density of a Euro coin and a Five Euro bill
    coin_weight = 7.5 # in grams
    coin_volume = 0.19 # in cm^3
    coin_density = coin_weight / coin_volume # in g/cm^3
    bill_weight = 0.6 # in grams
    bill_volume = 72.0 # in cm^3
    bill_density = bill_weight / bill_volume # in g/cm^3
    # Check if the density of the coin is greater than that of water
    if coin_density > 1.0:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())