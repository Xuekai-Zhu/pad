def solution():
   """Tommy wants to earn enough money to buy 8 new books. Each book costs $5. If Tommy already has $13, how much does he need to save up?"""
   num_books = 8
   book_cost = 5
   current_savings = 13
   total_cost = num_books * book_cost
   remaining_cost = total_cost - current_savings
   result = remaining_cost
   return result

print(solution())