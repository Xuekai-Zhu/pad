def solution():
    # Calculate cost of local call
    local_call_cost = 0.05 * 45

    # Calculate cost of international call
    international_call_cost = 0.25 * 31

    # Calculate total cost
    total_cost = local_call_cost + international_call_cost

    # Round to two decimal places
    result = round(total_cost, 2)

    return result

print(solution())