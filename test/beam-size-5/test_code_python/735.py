def solution():
    
    # Define the cost of a gallon jar
    GALLON_PRICE = 5

    # Calculate the cost of a half-gallon jar
    half_gallon_cost = GALLON_PRICE + 2

    # Calculate the total cost of 10-gallon jars
    total_cost_10_gallons = 10 * GALLON_PRICE

    # Calculate the total cost of 16 half-gallon jars
    total_cost_16_gallons = 16 * HALF_GALLON_PRICE

    # Calculate the total cost of all the jars
    total_cost = total_cost_10_gallons + total_cost_16_gallons

    # Display the total cost
    result = total_cost
    return result

print(solution())