def solution():
    # Calculate the distance Jenna drove in total
    distance = (2 * 60) + (3 * 50)  # distance = time * speed

    # Calculate the amount of gas needed for the trip
    gas_needed = distance / 30  # 30 miles per gallon

    # Calculate how much money Jenna spends on gas
    cost_of_gas = gas_needed * 2  # $2 per gallon

    result = cost_of_gas
    return result

print(solution())