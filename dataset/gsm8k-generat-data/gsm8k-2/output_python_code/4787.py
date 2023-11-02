def solution():
    """Fran's school just instituted a school uniform policy. Each student needs to buy five complete uniforms, each consisting of pants, shirt, tie and socks. The pants cost $20, the shirt costs twice as much as the pants, the tie costs 1/5 as much as the shirt and the socks cost $3/pair. How many dollars will each student need to spend?"""
    num_uniforms = 5
    pants_cost = 20
    shirt_cost = 2 * pants_cost
    tie_cost = shirt_cost / 5
    socks_cost = 3
    total_cost_per_uniform = pants_cost + shirt_cost + tie_cost + (2 * socks_cost)
    total_cost_per_student = num_uniforms * total_cost_per_uniform
    result = total_cost_per_student
    return result

print(solution())