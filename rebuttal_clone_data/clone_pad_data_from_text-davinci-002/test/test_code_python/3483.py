def solution():
     cost_per_book = 20
     num_books = 20
     discount_threshold = 5
     discount_amount = 2
     
     if num_books > discount_threshold:
         total_cost = (num_books * cost_per_book) - ((num_books - discount_threshold) * discount_amount)
     else:
         total_cost = num_books * cost_per_book
         
     result = total_cost
     return result

print(solution())