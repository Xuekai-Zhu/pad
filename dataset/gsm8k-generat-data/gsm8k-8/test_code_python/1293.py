def solution():
    # Calculate the total cost of Jimmy's shorts
    jimmy_shorts_cost = 3 * 15
    jimmy_discount = jimmy_shorts_cost * 0.1
    jimmy_total_cost = jimmy_shorts_cost - jimmy_discount

    # Calculate the total cost of Irene's shirts
    irene_shirts_cost = 5 * 17
    irene_discount = irene_shirts_cost * 0.1
    irene_total_cost = irene_shirts_cost - irene_discount

    # Calculate the total cost of their purchases
    total_cost = jimmy_total_cost + irene_total_cost
    result = total_cost
    return result

print(solution())