def solution():
    """John has to replace the ball bearings for machines he works with. He has 10 machines and they take 30 ball bearings each. It normally costs $1 per ball bearing but right now there is a sale where they are only $.75. Also since he is buying in bulk he gets a further 20% discount. How much money did he save by buying them all during the sale rather than 1 at a time?"""
    num_machines = 10
    bearings_per_machine = 30
    original_price = 1
    sale_price = 0.75
    discount_percent = 20
    total_bearings = num_machines * bearings_per_machine
    original_cost = total_bearings * original_price
    sale_cost = total_bearings * sale_price
    saved_amount = original_cost - sale_cost
    saved_amount_with_discount = saved_amount * (discount_percent / 100)
    result = saved_amount_with_discount
    return result

print(solution())