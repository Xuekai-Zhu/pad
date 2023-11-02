def solution():
    books = [25.00, 18.00, 21.00, 35.00, 12.00, 10.00]
    total_cost = 0

    # Calculate the discounted cost for each book
    for book in books:
        if book > 22:
            discounted_cost = book * 0.7
        elif book < 20:
            discounted_cost = book * 0.8
        else:
            discounted_cost = book

        total_cost += discounted_cost  # Add the discounted cost to the total cost

    result = total_cost
    return result

print(solution())