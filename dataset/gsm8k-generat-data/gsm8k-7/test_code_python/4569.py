def solution():
    num_sheep = 8
    num_cattle = 5
    corn_price = 10
    grass_per_cattle_month = 2
    grass_per_sheep_month = 1
    corn_per_cattle_month = 1
    corn_per_sheep_month = 2
    total_grass = 144

    # Calculate the total grass consumed per month by all animals
    total_grass_consumed_per_month = (num_sheep * grass_per_sheep_month) + (num_cattle * grass_per_cattle_month)

    # Calculate the number of months that the animals can graze on the pasture
    num_months_on_pasture = total_grass / total_grass_consumed_per_month

    # Calculate the number of bags of corn needed for the remaining months
    total_corn_bags = ((num_sheep * corn_per_sheep_month) + (num_cattle * corn_per_cattle_month)) * (12 - num_months_on_pasture)

    # Calculate the total cost of the corn bags
    total_corn_cost = total_corn_bags * corn_price
    result = total_corn_cost
    return result

print(solution())