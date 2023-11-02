def solution():
    num_books = 3
    school_price = 45
    discount = 0.2  # 20% discount

    # Calculate the price per book outside the school
    outside_price = school_price * (1 - discount)

    # Calculate the total cost of buying 3 books from the school bookshop
    school_total = num_books * school_price

    # Calculate the total cost of buying 3 books from outside bookshops
    outside_total = num_books * outside_price

    # Calculate the amount Peter can save by buying from outside bookshops
    total_savings = school_total - outside_total
    result = total_savings
    return result

print(solution())