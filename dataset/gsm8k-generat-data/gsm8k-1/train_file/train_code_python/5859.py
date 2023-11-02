def solution():
    """Robe's car broke and he used $10 from his savings to pay for the repair. Before the repair, he bought 2 kinds of spare parts. 
    A corner light that costs twice the price of the repair fee, and two brake disks; each disk cost thrice the price of the corner light. 
    After that, he had $480 savings left. How much money did Robe have saved before his car broke?"""
    
    repair_fee = 10
    corner_light = repair_fee * 2
    brake_disks = corner_light * 3 * 2
    total_spent = repair_fee + corner_light + brake_disks
    remaining_savings = 480
    initial_savings = total_spent + remaining_savings
    result = initial_savings
    
    return result

print(solution())