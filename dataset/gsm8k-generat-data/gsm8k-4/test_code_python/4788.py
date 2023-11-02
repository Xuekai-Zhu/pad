def solution():
    """Fran's school just instituted a school uniform policy. Each student needs to buy five complete uniforms, each consisting of pants, shirt, tie and socks. The pants cost $20, the shirt costs twice as much as the pants, the tie costs 1/5 as much as the shirt and the socks cost $3/pair. How many dollars will each student need to spend?"""
    # Define the cost of each uniform item
    pants_cost = 20
    shirt_cost = pants_cost * 2
    tie_cost = shirt_cost / 5
    socks_cost = 3

    # Calculate the total cost of one complete uniform
    uniform_cost = pants_cost + shirt_cost + tie_cost + (2 * socks_cost)

    # Calculate the total cost of buying five complete uniforms
    total_cost = uniform_cost * 5

    result = total_cost
    return result

print(solution())