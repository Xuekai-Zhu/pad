def solution():
    # Calculate the total amount of money that Celine paid for borrowing the books
    book1_charge = 0.50 * 20  # Celine returned one book after 20 days
    book2_charge = 0.50 * 31  # May has 31 days, and Celine returned the second book at the end of May
    book3_charge = 0.50 * 31  # Same as book 2
    total_charge = book1_charge + book2_charge + book3_charge
    result = total_charge
    return result

print(solution())