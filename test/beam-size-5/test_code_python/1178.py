def solution():
    
    # Define the total cost and the number of schools
    total_cost = 227000
    num_schools = 3

    # Calculate the total number of books Bob can buy
    total_books = total_cost // 500

    # Calculate the number of books Bob can buy per school
    books_per_school = total_books // num_schools

    # Display the number of books Bob can buy per school
    result = books_per_school
    return result

print(solution())