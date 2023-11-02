def solution():
    # Calculate the cost of the first two books with a 25% discount
    discounted_cost = (13 + 15) - ((25/100) * (13 + 15))  # first two books cost 13.00 and 15.00 with a 25% discount

    # Calculate the total cost of the four books
    total_cost = discounted_cost + 10 + 10  # books 1 and 2 with discount plus books 3 and 4 at 10.00 each

    # Calculate the amount needed to reach the free shipping threshold
    additional_cost = 50 - total_cost

    result = additional_cost
    return result

print(solution())