def solution():
    book_price = 25
    pen_price = 4
    ruler_price = 1
    total_paid = 50

    # Calculate the total cost of all items
    total_cost = book_price + pen_price + ruler_price

    # Calculate the amount of change that Jay received
    change = total_paid - total_cost
    result = change
    return result

print(solution())