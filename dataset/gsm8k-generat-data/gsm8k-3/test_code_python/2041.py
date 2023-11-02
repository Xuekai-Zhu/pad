def solution():
    """Tony has a bucket that holds 2 pounds of sand. He has a sandbox out back that is two feet deep, four feet wide, and 5 feet long. A cubic foot of sand weighs 3 pounds. Because it's hot outside, he wants to make sure he stays hydrated, so every 4 trips he takes he drinks 3 ounces of bottled water. A 15 ounce bottle of water costs $2. He has $10 with him. How much change will he have after he buys all the water he needs?"""

    # Define the volume of the sandbox
    sandbox_volume = 2 * 4 * 5  # 40 cubic feet

    # Define the weight of the sand in the sandbox
    sand_weight = sandbox_volume * 3  # 120 pounds

    # Calculate the number of trips Tony needs to make to fill the sandbox
    trips_needed = int(sand_weight / 2)  # Each trip brings 2 pounds of sand

    # Calculate the number of water bottles Tony needs to buy
    bottles_needed = (trips_needed // 4) * 3  # Every 4 trips, he drinks 3 ounces of water

    # Calculate the cost of the water bottles
    cost_of_water = bottles_needed / 5 * 2  # Each 15 ounce bottle costs $2

    # Calculate the change Tony will have
    change = 10 - cost_of_water

    # Display the change Tony will have
    result = change
    return result

print(solution())