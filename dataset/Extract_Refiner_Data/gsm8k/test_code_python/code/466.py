def solution():
    
    pen_price = 2
    paper_price = 3 * pen_price - 1
    total_cost = pen_price + paper_price
    amount_paid = 10
    change = amount_paid - total_cost
    result = change
    return result

print(solution())