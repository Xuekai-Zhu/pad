def solution():
    washer_cost = 4
    dryer_cost_per_minute = 0.25/6  # 1 quarter for 10 minutes, so 1/4*1/60 = 1/240 per minute
    num_washloads = 2
    num_dryers = 3
    dryer_runtime = 40  # minutes

    # Calculate the total cost of using the washers
    total_washer_cost = num_washloads * washer_cost

    # Calculate the total cost of using the dryers
    total_dryer_cost = num_dryers * dryer_cost_per_minute * dryer_runtime

    # Calculate the total cost of doing laundry
    total_cost = total_washer_cost + total_dryer_cost
    result = total_cost
    return result

print(solution())