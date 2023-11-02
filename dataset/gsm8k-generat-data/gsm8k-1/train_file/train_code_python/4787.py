def solution():
    """Fran's school just instituted a school uniform policy. Each student needs to buy five complete uniforms, each consisting of pants, shirt, tie and socks. The pants cost $20, the shirt costs twice as much as the pants, the tie costs 1/5 as much as the shirt and the socks cost $3/pair. How many dollars will each student need to spend?"""
    number_of_uniforms = 5
    pant_cost = 20
    shirt_cost = pant_cost * 2
    tie_cost = shirt_cost * (1/5)
    socks_cost = 3
    cost_per_uniform = pant_cost + shirt_cost + tie_cost + (socks_cost * 2)
    total_cost = cost_per_uniform * number_of_uniforms
    result = total_cost
    return result

print(solution())