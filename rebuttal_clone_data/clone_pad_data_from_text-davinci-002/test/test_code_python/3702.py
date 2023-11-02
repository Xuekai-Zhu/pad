def solution():
     cost_tshirt = 20
     cost_pants = 80
     cost_shoes = 150
     discount = 10
     tshirt_total = cost_tshirt * 4
     pants_total = cost_pants * 3
     shoes_total = cost_shoes * 2
     total_before_discount = tshirt_total + pants_total + shoes_total
     total_after_discount = total_before_discount - (total_before_discount * (discount/100))
     result = total_after_discount
     return result

print(solution())