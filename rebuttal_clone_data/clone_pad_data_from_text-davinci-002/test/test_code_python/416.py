def solution():
    cost_per_book = 20
    books_bought = 3
    monthly_books_bought = books_bought * 12
    total_yearly_cost = cost_per_book * monthly_books_bought
    sale_price = 500
    loss = total_yearly_cost - sale_price
    result = loss
    return result

print(solution())