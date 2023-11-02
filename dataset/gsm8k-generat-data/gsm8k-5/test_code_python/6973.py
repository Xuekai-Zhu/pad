def solution():
    tank_capacity = 4000  # The tank has a capacity of 4000 gallons
    water_rate = 10  # The pipe fills the tank with water at a rate of 10 gallons per hour
    target_capacity = 0.75 * tank_capacity  # Mack wants to fill the tank to 3/4 of its capacity

    # Calculate the time it will take to fill the tank to the target capacity
    time = (target_capacity - 0) / water_rate

    result = time
    return result

print(solution())