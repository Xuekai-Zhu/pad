def solution():
    # Calculate the total number of books John has written
    total_books = 20 * 12 // 2  # John writes a book every 2 months for 20 years

    # Calculate the total amount of money John has made
    total_money = total_books * 30000  # John earns $30,000 per book

    result = total_money
    return result

print(solution())