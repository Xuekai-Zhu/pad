def solution():
    boxes_of_pizza = 5  # number of pizza boxes ordered
    cost_of_box = 7  # cost of each pizza box
    total_cost = boxes_of_pizza * cost_of_box  # total cost of the pizza order
    tip = (1/7) * total_cost  # tip amount
    total_payment = total_cost + tip  # total payment including tip
    change = 100 - total_payment  # change received by Allen
    result = change
    return result

print(solution())