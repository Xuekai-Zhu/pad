def solution():
    """Peter purchased 20 popsicles at $0.25 each. He also purchased 4 ice cream bars at $0.50 each. How much did he pay in total in dollars?"""
    popsicle_price = 0.25
    ice_cream_price = 0.5
    num_popsicles = 20
    num_ice_cream = 4
    total_cost = (popsicle_price * num_popsicles) + (ice_cream_price * num_ice_cream)
    result = total_cost
    return result

print(solution())