def solution():
    """Very early this morning, Elise left home in a cab headed for the hospital. Fortunately, the roads were clear, and the cab company only charged her a base price of $3, and $4 for every mile she traveled. If Elise paid a total of $23, how far is the hospital from her house?"""
    # Define the base price and per-mile cost
    BASE_PRICE = 3
    PER_MILE_COST = 4

    # Define the total cost of the trip
    TOTAL_COST = 23

    # Calculate the cost of the distance traveled
    distance_cost = TOTAL_COST - BASE_PRICE

    # Calculate the distance traveled
    distance = distance_cost / PER_MILE_COST

    # Display the distance
    result = distance
    return result

print(solution())