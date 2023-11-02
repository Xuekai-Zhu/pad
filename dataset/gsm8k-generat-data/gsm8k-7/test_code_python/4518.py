def solution():
    city_distance = 60
    highway_distance = 200
    city_mpg = 30
    highway_mpg = 40
    gas_price = 3.0

    # Calculate the total amount of gas required for the city portion
    city_gas = city_distance / city_mpg

    # Calculate the total amount of gas required for the highway portion
    highway_gas = highway_distance / highway_mpg

    # Calculate the total amount of gas required for the entire trip
    total_gas = city_gas + highway_gas

    # Calculate the total cost of gas for the entire trip
    total_cost = total_gas * gas_price
    result = total_cost
    return result

print(solution())