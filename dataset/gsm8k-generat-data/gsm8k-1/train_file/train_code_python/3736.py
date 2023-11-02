def solution():
    """Patricia has 4 barrels of 7 gallons each. All of them are empty, and there's only one faucet with a flow rate of 3.5 gallons per minute. How many minutes will it take to fill all 4 barrels?"""
    barrels = 4
    capacity = 7
    total_gallons = barrels * capacity
    flow_rate = 3.5
    minutes = total_gallons / flow_rate
    result = minutes
    return result

print(solution())