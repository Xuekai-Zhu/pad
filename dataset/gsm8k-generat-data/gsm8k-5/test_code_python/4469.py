def solution():
    num_english_books = 35
    num_geography_books = 35
    cost_english_books = 7.50
    cost_geography_books = 10.50

    # Calculate the total cost of the order
    total_cost = (num_english_books * cost_english_books) + (num_geography_books * cost_geography_books)

    result = total_cost
    return result

print(solution())