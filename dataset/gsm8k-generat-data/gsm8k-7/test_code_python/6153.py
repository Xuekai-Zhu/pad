def solution():
    num_books = 20
    base_price = 20
    discount = 2
    num_discounted_books = num_books - 5

    # Calculate the total cost of the first 5 books
    total_cost = base_price * 5

    # Calculate the total cost of the remaining books with discount
    for i in range(num_discounted_books):
        if i < 15:
            total_cost += base_price + i*discount
        else:
            total_cost += base_price + 15*discount

    result = total_cost
    return result

print(solution())