def solution(): 
    """Connor wanted to order some new books to read. The website was offering free shipping over $50.00. They also had a deal that when you buy 4 books; the first two were 25% off. Book 1 cost 13.00 and Book 2 cost 15.00. Book 3 & 4 were both $10.00 each. How much more money did Connor need to spend to receive free shipping?"""
    total_cost = 13 + 15 + 10 + 10
    discount = 0.25 * (13 + 15)
    total_cost = total_cost - discount
    shipping_cost = 0
    if total_cost < 50:
        shipping_cost = 7.99
    
    additional_spending = 50 - total_cost + shipping_cost
    result = additional_spending
    return result

print(solution())