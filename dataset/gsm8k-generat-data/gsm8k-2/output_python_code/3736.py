def solution():
    """Patricia has 4 barrels of 7 gallons each. All of them are empty, and there's only one faucet with a flow rate of 3.5 gallons per minute. How many minutes will it take to fill all 4 barrels?"""
    barrel_size = 7
    num_barrels = 4
    total_volume = barrel_size * num_barrels
    flow_rate = 3.5
    time = total_volume / flow_rate
    result = time
    return result

print(solution())