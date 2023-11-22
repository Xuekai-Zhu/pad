def solution():
    
    # Define the prices of wooden tables and roof frames
    wooden_price = 20
    roof_price = 10

    # Define the number of wooden tables and roof frames
    num_wooden_tables = 4
    num_roof_frames = 2

    # Calculate the total cost of wooden tables and roof frames
    total_wooden_cost = wooden_price * num_wooden_tables
    total_roof_cost = roof_price * num_roof_frames
    total_cost = total_wooden_cost + total_roof_cost

    # return the result
    result = total_cost
    return result

print(solution())