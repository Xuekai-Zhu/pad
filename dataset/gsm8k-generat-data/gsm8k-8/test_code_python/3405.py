def solution():
    # Define the number of shirts and pants
    num_shirts = 10
    num_pants = 12

    # Calculate the time it takes to fix each item
    shirt_time = 1.5
    pants_time = 2 * shirt_time

    # Calculate the total time it takes to fix all the items
    total_time = num_shirts * shirt_time + num_pants * pants_time

    # Calculate the total cost
    hourly_rate = 30
    total_cost = total_time * hourly_rate

    result = total_cost
    return result

print(solution())