def solution():
    lemons = 6
    papayas = 4
    mangos = 2
    lemon_cost = 2
    papaya_cost = 1
    mango_cost = 4
    discount = 1
    total_cost = (lemons * lemon_cost) + (papayas * papaya_cost) + (mangos * mango_cost) - (discount * ((lemons + papayas + mangos) // 4))
    result = total_cost
    return result

print(solution())