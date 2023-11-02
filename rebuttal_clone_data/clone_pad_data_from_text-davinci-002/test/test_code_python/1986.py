def solution():

    cost_per_day = 0.5
    days_borrowed_1 = 20
    days_borrowed_2 = 31
    cost_book_1 = cost_per_day * days_borrowed_1
    cost_book_2 = cost_per_day * days_borrowed_2
    cost_book_3 = cost_per_day * days_borrowed_2
    total_cost = cost_book_1 + cost_book_2 + cost_book_3
    result = total_cost
    return result

print(solution())