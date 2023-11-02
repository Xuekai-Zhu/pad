def solution():
    # Calculate the capacity of Catherine's water heater
    capacity_Catherine = 40/2  # Wallace's water heater is twice the size of Catherine's water heater
    # Calculate the total number of gallons of water they both have when their water heaters are 3/4 full
    total_gallons = (3/4)*(40) + (3/4)*(capacity_Catherine)
    result = total_gallons
    return result

print(solution())