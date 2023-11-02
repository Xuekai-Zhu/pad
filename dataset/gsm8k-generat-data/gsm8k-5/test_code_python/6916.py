def solution():
    cost = 50  # Book costs $50
    marked_price = cost * 1.3  # Book is marked 30% above the cost
    discounted_price = marked_price * 0.9  # Book is given a 10% discount

    # Calculate the profit percentage
    profit = discounted_price - cost
    profit_percentage = (profit / cost) * 100
    result = profit_percentage
    return result

print(solution())