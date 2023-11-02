def solution():
    distance = 10 + 6 + 5 + 9 # total distance in miles
    miles_per_gallon = 15
    cost_per_gallon = 3.5
    
    # Calculate the total gallons of gas needed for the entire trip
    total_gallons = distance / miles_per_gallon
    
    # Calculate the total cost of the gas for the entire trip
    total_cost = total_gallons * cost_per_gallon
    result = total_cost
    return result

print(solution())