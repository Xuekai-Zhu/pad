def solution():
     cost = 40
     percentage_discount = 25
     discount = cost * (percentage_discount / 100)
     cost_after_discount = cost - discount
     number_of_mani_pedis = 5
     total_cost = cost_after_discount * number_of_mani_pedis
     result = total_cost
     return result

print(solution())