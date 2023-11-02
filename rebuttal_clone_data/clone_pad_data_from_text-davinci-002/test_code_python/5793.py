def solution():
    toy_cost = 12
    toys_bought = 4
    toy_discount = .5
    total_cost = (toy_cost * toys_bought) - ((toy_cost * toys_bought) * toy_discount)
    result = total_cost
    return result

print(solution())