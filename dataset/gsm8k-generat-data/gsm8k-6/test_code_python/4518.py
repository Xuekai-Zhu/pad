def solution(): 
    # Calculate the total number of gallons needed for the trip
    city_gallons = 60 / 30  # number of gallons needed for 60 city miles
    highway_gallons = 200 / 40  # number of gallons needed for 200 highway miles
    total_gallons = city_gallons + highway_gallons  # total number of gallons needed for the trip
    
    # Calculate the total cost for the trip
    cost_per_gallon = 3.00  # cost of gas per gallon
    total_cost = total_gallons * cost_per_gallon  # total cost for the trip
    
    result = total_cost
    return result

print(solution())