def solution():
    """A local gas station is selling gas for $3.00 a gallon. An app company is offering $.20 cashback per gallon if you fill up at this station. If someone buys 10 gallons of gas, how much with their gas be, after the cashback rewards?"""
    gas_price = 3.00
    cashback = .20
    gallons = 10
    total_cost = (gas_price * gallons) - (cashback * gallons)
    result = total_cost
    return result

print(solution())