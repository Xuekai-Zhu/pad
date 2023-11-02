def solution():
    # Calculate the volume of the sandbox
    sandbox_volume = 2 * 4 * 5  # 2 feet deep, 4 feet wide, and 5 feet long

    # Calculate the weight of sand needed to fill the sandbox
    sand_weight = sandbox_volume * 3  # a cubic foot of sand weighs 3 pounds

    # Calculate the number of trips Tony needs to make to fill the sandbox
    trips = sand_weight // 2  # the bucket holds 2 pounds of sand

    # Calculate the number of bottles of water Tony needs to drink
    water_bottles = trips // 4 + 1  # every 4 trips he drinks 3 ounces, round up to the nearest bottle

    # Calculate the total cost of the water
    water_cost = water_bottles * 2  # each bottle costs $2

    # Calculate the change Tony will have
    change = 10 - water_cost

    result = change
    return result

print(solution())