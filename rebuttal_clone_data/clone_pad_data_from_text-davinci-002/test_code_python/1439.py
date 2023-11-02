def solution():
     cost_of_pizzas = 10 * 4
     delivery_tip = 5
     total_cost = cost_of_pizzas + delivery_tip
     change_received = 50 - total_cost
     result = change_received
     return result

print(solution())