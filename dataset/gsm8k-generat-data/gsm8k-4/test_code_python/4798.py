def solution():
    """This morning, farmer Rita's workers collected 30,000 gallons of milk and chilled it in a storage tank. They then spent the next 4 hours pumping milk at a rate of 2,880 gallons/hour from the storage tank into a milk tanker. For the next 7 hours, the workers added more milk into the storage tank, at a rate of 1,500 gallons per hour. How many gallons of milk were left in the storage tank?"""
    # Define the initial amount of milk collected
    initial_milk = 30000

    # Calculate the amount of milk pumped out of the storage tank
    pumped_milk = 2880 * 4

    # Calculate the amount of milk added to the storage tank after pumping
    added_milk = 1500 * 7

    # Calculate the amount of milk left in the storage tank
    remaining_milk = initial_milk - pumped_milk + added_milk

    # return the result
    result = remaining_milk
    return result

print(solution())