def solution():
    # Calculate the total distance Carla needs to drive
    total_distance = 8 + 6 + 12 + 2*(12-6)  # twice the distance from the school to soccer practice because she has to do a round trip

    # Calculate how many gallons of gas Carla will need
    gas_needed = total_distance / 25

    # Calculate how much Carla will have to spend on gas
    gas_cost = gas_needed * 2.5

    result = gas_cost
    return result

print(solution())