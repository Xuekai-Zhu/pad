def solution():
    num_discounted_books = 5
    discounted_books_price = 10

    num_online_books = 2
    online_books_price = 40

    num_store_books = 3
    store_books_price = online_books_price * 3

    # Calculate the total cost of all discounted books
    total_discounted_cost = num_discounted_books * discounted_books_price

    # Calculate the total cost of all online ordered books
    total_online_cost = num_online_books * online_books_price

    # Calculate the total cost of all books bought from the bookstore
    total_store_cost = num_store_books * store_books_price

    # Calculate the total cost of all textbooks
    total_cost = total_discounted_cost + total_online_cost + total_store_cost
    result = total_cost
    return result

print(solution())