def solution():
    # Calculate the volume of the sandbox in cubic feet
    sandbox_volume = 2 * 4 * 5

    # Calculate the weight of the sand needed in pounds
    sand_weight = sandbox_volume * 3

    # Calculate the number of trips Tony will make to fill the bucket
    num_trips = sand_weight // 2 + (1 if sand_weight % 2 != 0 else 0)

    # Calculate the number of bottles of water Tony will need to buy
    num_bottles = num_trips // 4 + (1 if num_trips % 4 != 0 else 0)

    # Calculate the total cost of the water
    total_cost = num_bottles * 2

    # Calculate the change Tony will have after buying the water
    change = 10 - total_cost
    result = change
    return result

print(solution())