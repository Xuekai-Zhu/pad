def solution():
    """Juanita goes through 1 bottle of sunscreen a month. She likes to stock up for the entire year when a certain website offers 30% off her entire purchase. If each bottle is $30.00 how much will all of the sunscreen cost after the discount?"""
    # Calculate the cost of 12 bottles of sunscreen without discount
    cost_without_discount = 30 * 12

    # Calculate the discount using the discount percentage
    discount = cost_without_discount * 0.3

    # Calculate the cost of 12 bottles of sunscreen with discount
    cost_with_discount = cost_without_discount - discount

    # Return the result
    result = cost_with_discount
    return result

print(solution())