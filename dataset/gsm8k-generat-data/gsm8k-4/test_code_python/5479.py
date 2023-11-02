def solution():
    """A guy goes to the tool shop and buys 5 sets of drill bits. Each set cost 6 dollars. He then pays 10% tax on the order. What was the total amount he paid?"""
    # Define the cost of each drill bit set and the number of sets purchased
    drill_bit_cost = 6
    num_sets = 5

    # Calculate the subtotal and the tax amount
    subtotal = drill_bit_cost * num_sets
    tax = subtotal * 0.1

    # Calculate the total amount paid
    total = subtotal + tax

    result = total
    return result

print(solution())