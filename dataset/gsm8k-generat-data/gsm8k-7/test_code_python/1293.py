def solution():
    jimmy_shorts = 3
    jimmy_shorts_price = 15

    irene_shirts = 5
    irene_shirts_price = 17

    # Calculate the total cost of Jimmy's shorts
    jimmy_shorts_cost = jimmy_shorts * jimmy_shorts_price

    # Calculate the total cost of Irene's shirts
    irene_shirts_cost = irene_shirts * irene_shirts_price

    # Calculate the total cost before discount
    total_cost_before_discount = jimmy_shorts_cost + irene_shirts_cost

    # Calculate the discount amount
    discount = 0.1  # 10% discount for seniors
    discount_amount = total_cost_before_discount * discount

    # Calculate the total cost after discount
    total_cost_after_discount = total_cost_before_discount - discount_amount
    result = total_cost_after_discount
    return result

print(solution())