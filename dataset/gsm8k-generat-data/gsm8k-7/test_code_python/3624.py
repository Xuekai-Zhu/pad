def solution():
    mpg = 3
    distance_to_cheaper_gas = 90
    current_gas = 12

    # Calculate the remaining distance the truck can go with current gas
    current_distance = current_gas * mpg

    # Calculate the distance the truck still needs to cover
    remaining_distance = distance_to_cheaper_gas - current_distance

    # Calculate the amount of gas needed to cover the remaining distance
    additional_gas = remaining_distance / mpg
    result = additional_gas
    return result

print(solution())