def solution():
    """A pound of almonds costs $10 while a pound of walnuts costs $15. How much more does it cost for a mixture of 1/2 pound almonds and 1/3 pound walnuts than a mixture of 1/5 pound almonds and 1/3 pound walnuts?"""
    almond_cost = 10
    walnut_cost = 15
    mix1_almonds = 1/2
    mix1_walnuts = 1/3
    mix2_almonds = 1/5
    mix2_walnuts = 1/3
    
    mix1_cost = (mix1_almonds * almond_cost) + (mix1_walnuts * walnut_cost)
    mix2_cost = (mix2_almonds * almond_cost) + (mix2_walnuts * walnut_cost)
    difference = mix1_cost - mix2_cost

    result = difference
    return result

print(solution())