def solution():
    
    # Define the cost of a gallon jar and a half-gallon jar
    GALLON_PRICE = 5
    HALF_PRICE = GALLON_PRICE / 2

    # Calculate the total cost of 10-gallon jars and 16 half-gallon jars
    total_cost = (10 * GALLON_PRICE) + (16 * HALF_PRICE)

    # Display the total cost
    result = total_cost
    return result

print(solution())