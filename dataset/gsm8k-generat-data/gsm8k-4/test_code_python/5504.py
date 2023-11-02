def solution():
    """Thomas owns 200 books. He decides to sell them and use the money to buy records. Each book sells for $1.5. A record costs $3. If he buys 75 records, how much money does he have left over?"""
    # Define the initial number of books and the price per book
    INITIAL_BOOKS = 200
    BOOK_PRICE = 1.5

    # Define the number of records to be purchased and the price per record
    RECORDS_TO_PURCHASE = 75
    RECORD_PRICE = 3

    # Calculate the total earnings from selling the books
    total_earnings = INITIAL_BOOKS * BOOK_PRICE

    # Calculate the cost of purchasing the records
    records_cost = RECORDS_TO_PURCHASE * RECORD_PRICE

    # Calculate the money left over
    money_left = total_earnings - records_cost

    # return the result
    result = money_left
    return result

print(solution())