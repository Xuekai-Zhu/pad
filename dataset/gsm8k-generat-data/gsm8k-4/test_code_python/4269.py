def solution():
    """Timothy decides he wants to start living off the land. He buys 30 acres of land for $20 an acre. He then builds himself a large house for $120,000. After that, he gets himself 20 cows for $1000 per cow and 100 chickens for $5 per chicken. The last thing is solar panels which take 6 hours to install with an installation cost of $100 an hour and then a flat fee of $6000 for the equipment. How much did everything cost?"""
    # Define the cost of land, house, cows, chickens, and solar panels
    land_cost = 30 * 20
    house_cost = 120000
    cow_cost = 20 * 1000
    chicken_cost = 100 * 5
    solar_installation_cost = 6 * 100 + 6000

    # Calculate the total cost
    total_cost = land_cost + house_cost + cow_cost + chicken_cost + solar_installation_cost

    # return the result
    result = total_cost
    return result

print(solution())