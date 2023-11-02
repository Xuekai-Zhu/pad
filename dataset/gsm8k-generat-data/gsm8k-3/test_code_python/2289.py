def solution():
    """Connor wanted to order some new books to read.  The website was offering free shipping over $50.00.  They also had a deal that when you buy 4 books; the first two were 25% off.  Book 1 cost 13.00 and Book 2 cost 15.00.  Book 3 & 4 were both $10.00 each.  How much more money did Connor need to spend to receive free shipping?"""
    # Define the prices of each book
    BOOK1_PRICE = 13.00
    BOOK2_PRICE = 15.00
    BOOK3_PRICE = 10.00
    BOOK4_PRICE = 10.00

    # Calculate the total cost of the books before discounts
    total_cost = BOOK1_PRICE + BOOK2_PRICE + BOOK3_PRICE + BOOK4_PRICE

    # Calculate the discounted cost of the first two books
    discount = (BOOK1_PRICE + BOOK2_PRICE) * 0.25
    discounted_cost = BOOK1_PRICE + BOOK2_PRICE - discount

    # Calculate the total cost of the books after discounts
    total_cost_discounted = discounted_cost + (2 * BOOK3_PRICE) + (2 * BOOK4_PRICE)

    # Calculate the amount needed to spend for free shipping
    free_shipping_amount = 50.0

    # Calculate the difference between the total cost and free shipping amount
    difference = free_shipping_amount - total_cost_discounted

    # Display the difference
    result = difference
    return result

print(solution())