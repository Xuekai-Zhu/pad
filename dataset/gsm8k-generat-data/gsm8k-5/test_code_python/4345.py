def solution():
    regular_price = 9  # Cost of a regular ticket
    child_price = regular_price - 2  # Cost of a child ticket
    adult_count = 2  # There are 2 adults in the family
    total_cost = adult_count * regular_price + child_count * child_price  # Total cost of the tickets
    change = 1  # They received $1 change from two $20 bills
    cash_paid = 2 * 20  # They paid with two $20 bills

    # Calculate the cost of the tickets and the number of children
    child_count = (cash_paid - change - adult_count * regular_price) / child_price
    result = child_count
    return result

print(solution())