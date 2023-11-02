def solution():
    barrels = 4  # Patricia has 4 barrels
    gallons_per_barrel = 7  # Each barrel holds 7 gallons

    # Calculate the total number of gallons needed to fill all the barrels
    total_gallons = barrels * gallons_per_barrel

    flow_rate = 3.5  # The faucet has a flow rate of 3.5 gallons per minute

    # Calculate the number of minutes it will take to fill all the barrels
    filling_time = total_gallons / flow_rate
    result = filling_time
    return result

print(solution())