def solution():
    """Five friends eat at a fast-food chain and order the following: 5 pieces of hamburger that cost $3 each; 4 sets of French fries that cost $1.20; 5 cups of soda that cost $0.5 each; and 1 platter of spaghetti that cost $2.7. How much will each of them pay if they will split the bill equally?"""
    # Define the prices of the items ordered
    hamburger_price = 3
    fries_price = 1.2
    soda_price = 0.5
    spaghetti_price = 2.7

    # Calculate the total cost of the items ordered
    total_cost = (5 * hamburger_price) + (4 * fries_price) + (5 * soda_price) + spaghetti_price

    # Calculate the cost per person if they split the bill equally
    cost_per_person = total_cost / 5

    result = cost_per_person
    return result

print(solution())