def solution():
    # Calculate the amount of gas needed for the city portion of the trip
    city_gas = 60/30

    # Calculate the amount of gas needed for the highway portion of the trip
    highway_gas = 200/40

    # Calculate the total amount of gas needed, in gallons
    total_gas = city_gas + highway_gas

    # Calculate the total cost of the gas
    total_cost = total_gas * 3.00

    result = total_cost
    return result

print(solution())