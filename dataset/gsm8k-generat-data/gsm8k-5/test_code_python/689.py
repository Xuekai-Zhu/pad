def solution():
    # Calculate the cost of the Lyft ride
    lyft_cost = 22 - 3 - 4  # Uber ride costs $3 more than a Lyft and a Lyft ride costs $4 more than a taxi
    # Calculate the cost of the taxi ride plus the tip
    taxi_cost = (lyft_cost - 4) * 1.2  # The cost of the taxi ride plus a 20% tip

    # Calculate the total cost of the ride downtown
    total_cost = taxi_cost + (lyft_cost - 4)
    result = total_cost
    return result

print(solution())