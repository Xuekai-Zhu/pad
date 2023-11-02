def solution():
    """This morning, farmer Rita's workers collected 30,000 gallons of milk and chilled it in a storage tank. They then spent the next 4 hours pumping milk at a rate of 2,880 gallons/hour from the storage tank into a milk tanker. For the next 7 hours, the workers added more milk into the storage tank, at a rate of 1,500 gallons per hour. How many gallons of milk were left in the storage tank?"""
    initial_milk = 30000
    pumped_out = 2880 * 4
    added_back = 1500 * 7
    remaining_milk = initial_milk - pumped_out + added_back
    result = remaining_milk
    return result

print(solution())