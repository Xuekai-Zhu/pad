def solution():
     pens = 5
     notebooks = 3
     binders = 1
     highlighters = 2
     num_students = 30
     
     pen_price = 0.50
     notebook_price = 1.25
     binder_price = 4.25
     highlighter_price = 0.75
     
     pen_total = pens * pen_price * num_students
     notebook_total = notebooks * notebook_price * num_students
     binder_total = binders * binder_price * num_students
     highlighter_total = highlighters * highlighter_price * num_students
     
     total_cost = pen_total + notebook_total + binder_total + highlighter_total
     
     teacher_discount = 100
     total_after_discount = total_cost - teacher_discount
     
     result = total_after_discount
     
     return result

print(solution())