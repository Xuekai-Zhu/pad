def solution():
    """A guy goes to the tool shop and buys 5 sets of drill bits. Each set cost 6 dollars. He then pays 10% tax on the order. What was the total amount he paid?"""
    num_sets = 5
    set_price = 6
    subtotal = num_sets * set_price
    tax_rate = 0.1
    tax = subtotal * tax_rate
    total_price = subtotal + tax
    result = total_price
    return result

print(solution())