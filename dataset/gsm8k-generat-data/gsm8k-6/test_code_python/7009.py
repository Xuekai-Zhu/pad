def solution():
    # Calculate the total amount of money earned by Pablo
    money_earned = 15.03 - 0.03  # Pablo spent $15 and had $3 left over, so he earned $15.03
    cost_per_book = 150 / 100  # Pablo earns 1 cent per page, which is equivalent to 1/100 dollar per page
    num_books = money_earned / cost_per_book  # Divide the total money earned by the cost of one book
    result = int(num_books)  # Round down to the nearest whole number of books
    return result

print(solution())