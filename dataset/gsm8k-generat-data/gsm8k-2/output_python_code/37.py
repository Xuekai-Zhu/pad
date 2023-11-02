def solution():
    """Five friends eat at a fast-food chain and order the following: 5 pieces of hamburger that cost $3 each; 4 sets of French fries that cost $1.20; 5 cups of soda that cost $0.5 each; and 1 platter of spaghetti that cost $2.7. How much will each of them pay if they will split the bill equally?"""
    hamburgers = 5
    hamburger_cost = 3
    fries_sets = 4
    fries_cost = 1.2
    sodas = 5
    soda_cost = 0.5
    spaghetti_cost = 2.7
    total_cost = (hamburgers * hamburger_cost) + (fries_sets * fries_cost) + (sodas * soda_cost) + spaghetti_cost
    total_friends = 5
    cost_per_friend = total_cost / total_friends
    result = cost_per_friend
    return result

print(solution())