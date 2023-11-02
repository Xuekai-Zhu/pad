def solution():
     """Ann, Bill, Cate, and Dale each buy personal pan pizzas cut into 4 pieces. If Bill and Dale eat 50% of their pizzas and Ann and Cate eat 75% of the pizzas, how many pizza pieces are left uneaten?"""
     people = 4
     bill_and_dale_eaten = 2
     ann_and_cate_eaten = 3
     total_eaten = bill_and_dale_eaten + ann_and_cate_eaten
     pieces_left = people * 4 - total_eaten
     result = pieces_left
     return result

print(solution())