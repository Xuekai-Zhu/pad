def solution():
     rooms = 5
     primer = 30.00
     paint = 25.00
     
     primer_sale_price = primer - (primer * 0.20)
     total_primer_cost = primer_sale_price * rooms
     total_paint_cost = paint * rooms
     
     total_cost = total_primer_cost + total_paint_cost
     
     return total_cost

print(solution())