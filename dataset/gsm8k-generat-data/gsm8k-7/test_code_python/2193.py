def solution():
    num_members = 6
    snack_fee = 150
    hardcover_fee = 30
    paperback_fee = 12
    num_hardcover_books = 6
    num_paperback_books = 6

    # Calculate the total amount paid for snacks
    total_snack_fee = num_members * snack_fee

    # Calculate the total amount paid for hardcover books
    total_hardcover_fee = num_members * hardcover_fee * num_hardcover_books

    # Calculate the total amount paid for paperback books
    total_paperback_fee = num_members * paperback_fee * num_paperback_books

    # Calculate the total amount collected by Niles
    total_collected = total_snack_fee + total_hardcover_fee + total_paperback_fee

    result = total_collected
    return result

print(solution())