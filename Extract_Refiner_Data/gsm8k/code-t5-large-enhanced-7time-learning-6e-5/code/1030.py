def solution():
    
    # Define the initial amount of money Ted started with
    initial_money = 200

    # Define the cost of each book and pencil
    book_cost = 16
    pencil_cost = 6

    # Define the number of books and pencils Ted bought
    num_books = 3
    num_pencils = 3

    # Calculate the total cost of the books and pencils
    total_cost = (num_books * book_cost) + (num_pencils * pencil_cost)

    # Calculate the total amount of money Ted spent
    total_spent = initial_money + total_cost

    # return the result
    result = total_spent
    return result

print(solution())