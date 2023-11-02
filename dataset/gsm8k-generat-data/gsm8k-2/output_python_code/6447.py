def solution():
    """Six kids and two adults are going to the circus. Kid's tickets are on sale for only half of the adult tickets. The total cost is $50. How much is one kid's ticket?"""
    num_kids = 6
    num_adults = 2
    total_cost = 50
    cost_per_adult = x
    cost_per_kid = 0.5 * x
    total_kid_cost = num_kids * cost_per_kid
    total_adult_cost = num_adults * cost_per_adult
    total_cost = total_kid_cost + total_adult_cost

    # solve for x
    x = total_cost / (num_kids/2 + num_adults)

    result = cost_per_kid
    return result

print(solution())