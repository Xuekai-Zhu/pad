def solution():
    # Find the cost of 1 dozen apples for Tony and Arnold
    cost_1_dozen_apples_Tony = 7 / 2  
    cost_1_dozen_apples_Arnold = 5 / 1

    # Find the cost of 1 bunch of bananas for Tony and Arnold
    cost_1_bunch_bananas_Tony = 7 - (cost_1_dozen_apples_Tony * 2)
    cost_1_bunch_bananas_Arnold = 5 - cost_1_dozen_apples_Arnold

    # Find the average cost of 1 bunch of bananas for Tony and Arnold
    cost_1_bunch_bananas = (cost_1_bunch_bananas_Tony + cost_1_bunch_bananas_Arnold) / 2
    result = cost_1_bunch_bananas
    return result

print(solution())