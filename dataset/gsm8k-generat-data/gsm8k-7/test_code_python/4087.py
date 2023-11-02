def solution():
    available_funds = 20000 - 500 - 3*500
    cost_per_foot = 1500

    # Calculate the maximum length of boat that Mitch can buy
    max_length = available_funds // cost_per_foot
    result = max_length
    return result

print(solution())