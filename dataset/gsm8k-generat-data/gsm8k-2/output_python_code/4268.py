def solution():
    """Timothy decides he wants to start living off the land. He buys 30 acres of land for $20 an acre. He then builds himself a large house for $120,000. After that, he gets himself 20 cows for $1000 per cow and 100 chickens for $5 per chicken. The last thing is solar panels which take 6 hours to install with an installation cost of $100 an hour and then a flat fee of $6000 for the equipment. How much did everything cost?"""
    land_price = 30 * 20
    house_price = 120000
    cows_price = 20 * 1000
    chickens_price = 100 * 5
    solar_installation_price = 6 * 100 + 6000
    total_cost = land_price + house_price + cows_price + chickens_price + solar_installation_price
    result = total_cost
    return result

print(solution())