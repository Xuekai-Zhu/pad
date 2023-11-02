def solution():
     cost_of_sale_books = 10
     number_of_sale_books = 5
     cost_of_online_books = 40
     number_of_online_books = 2
     cost_of_bookstore_books = cost_of_online_books * 3
     number_of_bookstore_books = 3
     total_cost = (cost_of_sale_books * number_of_sale_books) + (cost_of_online_books * number_of_online_books) + (cost_of_bookstore_books * number_of_bookstore_books)
     result = total_cost
     return result

print(solution())