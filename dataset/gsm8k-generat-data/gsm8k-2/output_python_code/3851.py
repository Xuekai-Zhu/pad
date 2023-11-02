def solution():
    """John has to replace the ball bearings for machines he works with. He has 10 machines and they take 30 ball bearings each. It normally costs $1 per ball bearing but right now there is a sale where they are only $.75. Also since he is buying in bulk he gets a further 20% discount. How much money did he save by buying them all during the sale rather than 1 at a time?"""
    machines = 10
    bearings_per_machine = 30
    normal_price = 1
    sale_price = 0.75
    discount = 0.2
    normal_total_cost = machines * bearings_per_machine * normal_price
    sale_total_cost = machines * bearings_per_machine * sale_price * (1 - discount)
    saved_money = normal_total_cost - sale_total_cost
    result = saved_money
    return result

print(solution())