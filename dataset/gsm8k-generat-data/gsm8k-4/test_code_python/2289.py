def solution():
    """Connor wanted to order some new books to read. The website was offering free shipping over $50.00. They also had a deal that when you buy 4 books; the first two were 25% off. Book 1 cost 13.00 and Book 2 cost 15.00. Book 3 & 4 were both $10.00 each. How much more money did Connor need to spend to receive free shipping?"""
    # define the prices of the books
    book1 = 13.00
    book2 = 15.00
    book3 = 10.00
    book4 = 10.00

    # calculate the total cost of the books before discount
    total_cost = book1 + book2 + book3 + book4

    # apply the discount for the first two books
    discount = (book1 + book2) * 0.25
    total_discounted_cost = total_cost - discount

    # calculate the amount needed to reach free shipping
    amount_needed = 50.00 - total_discounted_cost 

    result = round(amount_needed, 2)
    return result

print(solution())