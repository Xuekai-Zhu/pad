def solution():
    # Calculate the cost of one complete uniform
    pant_cost = 20
    shirt_cost = 2 * pant_cost
    tie_cost = 1/5 * shirt_cost
    sock_cost = 3
    uniform_cost = pant_cost + shirt_cost + tie_cost + 2 * sock_cost

    # Calculate the total cost for five complete uniforms
    total_cost = 5 * uniform_cost

    result = total_cost
    return result

print(solution())