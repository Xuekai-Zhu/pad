def solution():
     books_sold = 10
     books_at_2 = 2/5 * books_sold
     books_at_2_50 = books_sold - books_at_2
     total_earned = (books_at_2 * 2) + (books_at_2_50 * 2.50)
     result = total_earned
     return result

print(solution())