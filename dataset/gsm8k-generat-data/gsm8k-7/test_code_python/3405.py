def solution():
    num_shirts = 10
    num_pants = 12
    shirt_time = 1.5
    pant_time = shirt_time * 2
    hourly_rate = 30.0

    # Calculate the total time to fix all shirts
    time_shirts = num_shirts * shirt_time

    # Calculate the total time to fix all pants
    time_pants = num_pants * pant_time

    # Calculate the total time to fix all clothing items
    total_time = time_shirts + time_pants

    # Calculate the total cost for the seamstress
    total_cost = total_time * hourly_rate
    result = total_cost
    return result

print(solution())