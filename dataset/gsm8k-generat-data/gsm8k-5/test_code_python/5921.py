def solution():
    # Calculate the cost of the call to Freddy's dad
    cost_local_call = 0.05 * 45  # 5 cents per minute for a 45-minute call

    # Calculate the cost of the call to Freddy's brother
    cost_international_call = 0.25 * 31  # 25 cents per minute for a 31-minute call

    # Calculate the total cost of the calls
    total_cost = cost_local_call + cost_international_call
    result = total_cost
    return result

print(solution())