def solution():
    # Calculate the cost of each complete uniform
    shirt_cost = 20 * 2  # shirt costs twice as much as the pants, so $40
    tie_cost = shirt_cost * (1/5)  # tie costs 1/5 as much as the shirt, so $8
    total_uniform_cost = 20 + shirt_cost + tie_cost + 2*3  # pants + shirt + tie + 2 pairs of socks at $3/pair, so $34
    # Calculate the total cost for 5 complete uniforms
    total_cost = total_uniform_cost * 5
    result = total_cost
    return result

print(solution())