def solution():
    """Five friends eat at a fast-food chain and order the following: 5 pieces of hamburger that cost $3 each; 4 sets of French fries that cost $1.20; 5 cups of soda that cost $0.5 each; and 1 platter of spaghetti that cost $2.7. How much will each of them pay if they will split the bill equally?"""
    # Calculate the total cost of the food and drinks
    total_cost = 5 * 3 + 4 * 1.20 + 5 * 0.5 + 2.7

    # Divide the total cost equally among the friends
    cost_per_person = total_cost / 5

    # Round the result to two decimal places
    result = round(cost_per_person, 2)
    return result

print(solution())