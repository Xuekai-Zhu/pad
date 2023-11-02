def solution():
    """John buys twice as many red ties as blue ties. The red ties cost 50% more than blue ties. He spent $200 on blue ties that cost $40 each. How much did he spend on ties?"""
    blue_ties = 5 # $200 / $40 per tie = 5 ties
    red_ties = blue_ties * 2
    blue_cost = 40 # given in problem
    red_cost = blue_cost * 1.5 # red ties cost 50% more than blue ties
    total_cost = (blue_ties * blue_cost) + (red_ties * red_cost)
    result = total_cost
    
    return result

print(solution())