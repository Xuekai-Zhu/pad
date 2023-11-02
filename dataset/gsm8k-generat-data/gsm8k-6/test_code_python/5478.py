def solution():
    # Calculate the initial amount of water in the tank
    initial_water = (2/5) * 100  # the tank is 2/5 filled with water

    # Calculate the total amount of water collected on the first two days
    total_collected = 15 + (15 + 5)  # 15 liters on first day, 20 liters on second day

    # Calculate the remaining amount of water needed to fill the tank
    remaining_water = 100 - initial_water - total_collected

    # The remaining amount of water was collected on the third day
    result = remaining_water
    return result

print(solution())