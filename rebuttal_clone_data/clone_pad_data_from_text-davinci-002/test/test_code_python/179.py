def solution():
     cost_of_books = 236
     number_of_books = 6
     money_left = 14
     cost_of_each_book = (cost_of_books - money_left) / number_of_books
     result = cost_of_each_book
     return result

print(solution())