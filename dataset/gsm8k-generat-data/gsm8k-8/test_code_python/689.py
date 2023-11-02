def solution():
    # Calculate the cost of a Lyft ride
    lyft_cost = 22 - 3

    # Calculate the cost of a taxi ride
    taxi_cost = lyft_cost - 4

    # Calculate the tip for the taxi ride
    taxi_tip = 0.2 * taxi_cost

    # Calculate the total cost of the taxi ride including tip
    total_cost = taxi_cost + taxi_tip
    result = total_cost
    return result

print(solution())