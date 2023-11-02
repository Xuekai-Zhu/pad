def solution():
    # Define the initial stock of books
    initial_stock = 800

    # Calculate the total number of books sold
    total_sold = 60 + 10 + 20 + 44 + 66

    # Calculate the number of books not sold
    not_sold = initial_stock - total_sold
    result = not_sold
    return result

print(solution())