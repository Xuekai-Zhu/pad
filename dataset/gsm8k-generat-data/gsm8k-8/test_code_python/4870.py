def solution():
    # Define the ticket prices
    adult_price = 26
    child_price = adult_price / 2

    # Calculate the total revenue from adult tickets
    adult_revenue = 183 * adult_price

    # Calculate the total revenue from child tickets
    child_revenue = 28 * child_price

    # Calculate the total revenue from the concert
    total_revenue = adult_revenue + child_revenue
    result = total_revenue
    return result

print(solution())