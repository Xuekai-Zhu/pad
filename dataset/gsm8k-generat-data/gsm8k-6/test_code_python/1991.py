def solution():
    # Calculate the total cost of the trip
    total_cost = 28 + 10 + 55 + 25  # cost of savings, parking, admission and meal pass

    # Calculate the cost of gas for the trip
    gas_cost = (165/30) * 3  # distance divided by mileage per gallon, multiplied by gas cost per gallon

    # Calculate the remaining amount Sally needs to save up
    remaining_cost = total_cost + gas_cost - 28  # subtract the amount she already has saved up

    result = remaining_cost
    return result

print(solution())