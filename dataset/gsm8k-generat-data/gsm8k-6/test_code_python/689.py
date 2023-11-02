def solution():
    # Calculate the cost of the Lyft ride
    lyft_cost = 22 - 3  # Uber ride is $3 more than Lyft ride
    # Calculate the cost of the taxi ride with tip
    taxi_cost = (lyft_cost - 4) * 1.2  # Lyft ride is $4 more than taxi ride and tip is 20% of original cost
    # Calculate the total cost of the ride
    total_cost = taxi_cost + (taxi_cost * 0.2)  # Add tip to the taxi cost
    result = total_cost
    return result

print(solution())