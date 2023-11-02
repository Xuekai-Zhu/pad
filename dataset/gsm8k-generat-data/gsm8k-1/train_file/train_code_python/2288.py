def solution():
    """Connor wanted to order some new books to read. The website was offering free shipping over $50.00. They also had a deal that when you buy 4 books; the first two were 25% off. Book 1 cost 13.00 and Book 2 cost 15.00. Book 3 & 4 were both $10.00 each. How much more money did Connor need to spend to receive free shipping?"""
    book1_cost = 13
    book2_cost = 15
    book3_cost = 10
    book4_cost = 10
    num_books_for_discount = 4
    discount_rate = 0.25

    # apply the discount to the first two books
    discounted_books_cost = book1_cost + book2_cost - (book1_cost + book2_cost) * discount_rate

    # calculate the total cost of the four books
    total_cost = discounted_books_cost + book3_cost + book4_cost

    # calculate the remaining amount needed to qualify for free shipping
    remaining_shipping_cost = 50 - total_cost
    result = remaining_shipping_cost
    return result

print(solution())