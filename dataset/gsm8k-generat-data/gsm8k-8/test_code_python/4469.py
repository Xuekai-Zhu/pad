def solution():
    # Define the number of English and Geography textbooks
    num_of_eng_books = 35
    num_of_geo_books = 35

    # Define the cost of one English and one Geography textbook
    cost_of_eng_book = 7.5
    cost_of_geo_book = 10.5

    # Calculate the total cost of the order
    total_cost = (num_of_eng_books * cost_of_eng_book) + (num_of_geo_books * cost_of_geo_book)

    result = total_cost
    return result

print(solution())