def solution():
    # Calculate the total ounces of coffee needed for 3 dozen donuts
    donuts = 36  # 1 dozen equals 12
    coffee = donuts * 2  # for each donut they need 2 ounces of coffee

    # Calculate the number of pots of coffee needed
    pots = coffee / 12  # every pot of coffee she makes contains 12 ounces

    # Calculate the total cost of the coffee
    cost = pots * 3  # every pot of coffee costs $3 to make
    result = cost
    return result

print(solution())