def solution():
    """Timothy decides he wants to start living off the land.  He buys 30 acres of land for $20 an acre.  He then builds himself a large house for $120,000. After that, he gets himself 20 cows for $1000 per cow and 100 chickens for $5 per chicken.  The last thing is solar panels which take 6 hours to install with an installation cost of $100 an hour and then a flat fee of $6000 for the equipment. How much did everything cost?"""
    # Calculate the cost of the land
    land_cost = 30 * 20

    # Calculate the cost of the house
    house_cost = 120000

    # Calculate the total cost of the animals
    cow_cost = 20 * 1000
    chicken_cost = 100 * 5
    animal_cost = cow_cost + chicken_cost

    # Calculate the cost of the solar panels
    installation_cost = 6 * 100
    equipment_cost = 6000
    solar_cost = installation_cost + equipment_cost

    # Calculate the total cost of everything
    total_cost = land_cost + house_cost + animal_cost + solar_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())