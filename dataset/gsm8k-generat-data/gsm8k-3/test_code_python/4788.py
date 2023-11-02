def solution():
    """Fran's school just instituted a school uniform policy. Each student needs to buy five complete uniforms, each consisting of pants, shirt, tie and socks. The pants cost $20, the shirt costs twice as much as the pants, the tie costs 1/5 as much as the shirt and the socks cost $3/pair. How many dollars will each student need to spend?"""
    
    # Define the cost of each item in a uniform
    PANTS_COST = 20
    SHIRT_COST = 2 * PANTS_COST
    TIE_COST = SHIRT_COST / 5
    SOCKS_COST = 3

    # Calculate the total cost of one uniform
    uniform_cost = PANTS_COST + SHIRT_COST + TIE_COST + 2*SOCKS_COST

    # Calculate the total cost of 5 complete uniforms
    total_cost = 5 * uniform_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())