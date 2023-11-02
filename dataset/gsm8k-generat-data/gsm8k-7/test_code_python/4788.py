def solution():
    num_uniforms = 5
    pants_price = 20
    shirt_price = 2 * pants_price
    tie_price = shirt_price / 5
    socks_price = 3

    # Calculate the total cost of a complete uniform
    total_uniform_cost = pants_price + shirt_price + tie_price + (2 * socks_price)

    # Calculate the total cost of all five uniforms
    total_cost = num_uniforms * total_uniform_cost
    result = total_cost
    return result

print(solution())