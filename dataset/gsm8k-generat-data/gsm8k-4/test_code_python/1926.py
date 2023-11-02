def solution():
    """James buys 10 boxes of Capri-sun. Each box has 6 pouches in it. If he paid $12 how many cents does each pouch cost?"""
    # Define the total number of pouches and the total cost of the purchase
    total_pouches = 10 * 6
    total_cost = 1200  # 12 dollars = 1200 cents

    # Calculate the cost per pouch in cents
    cost_per_pouch = total_cost / total_pouches

    # return the result
    result = cost_per_pouch
    return result

print(solution())