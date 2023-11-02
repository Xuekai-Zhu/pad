def solution():
    city_miles = 60
    highway_miles = 200
    gas_price = 3.00

    # Calculate the total gallons of gas required for the trip
    city_gallons = city_miles / 30
    highway_gallons = highway_miles / 40
    total_gallons = city_gallons + highway_gallons

    # Calculate the total cost of gas for the trip
    total_cost = total_gallons * gas_price
    result = total_cost
    return result

print(solution())