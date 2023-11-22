def solution():
    
    # Define the cost of each bottle of scotch and cognac
    SCOTCH_COST = 600
    CANCAC_COST = SCOTCH_COST * 1.5

    # Define the number of bottles of scotch and cognac purchased
    scotch_count = 10
    cognac_count = 2 * scotch_count

    # Calculate the total cost of the scotch and cognac purchased
    scotch_cost = scotch_count * SCOTCH_COST
    cognac_cost = cognac_count * CANCAC_COST
    total_cost = scotch_cost + cognac_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())