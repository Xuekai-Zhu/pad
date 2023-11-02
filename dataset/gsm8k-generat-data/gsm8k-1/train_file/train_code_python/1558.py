def solution():
    """Maci is planning for the new school year and goes to the store to buy pens. She needs ten blue pens and 15 red pens. If a blue pen costs ten cents each and a red pen costs twice as much as the blue pen, how much money does Maci pay for the pens?"""
    num_blue_pens = 10
    num_red_pens = 15
    cost_blue_pen = 0.1
    cost_red_pen = 2 * cost_blue_pen
    total_cost = (num_blue_pens * cost_blue_pen) + (num_red_pens * cost_red_pen)
    result = total_cost
    return result

print(solution())