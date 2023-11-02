def solution():
    """Thomas owns 200 books. He decides to sell them and use the money to buy records. Each book sells for $1.5. A record costs $3. If he buys 75 records, how much money does he have left over?"""
    # Define the number of books and their selling price
    num_books = 200
    book_price = 1.5

    # Define the number of records and their cost
    num_records = 75
    record_cost = 3

    # Calculate the total income from selling the books
    total_income = num_books * book_price

    # Calculate the total cost of buying the records
    total_cost = num_records * record_cost

    # Calculate the amount of money left over
    money_left_over = total_income - total_cost

    # Display the amount of money left over
    result = money_left_over
    return result

print(solution())