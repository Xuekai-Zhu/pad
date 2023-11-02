def solution():
    # Let x be the cost of a Reuben sandwich
    x = 0

    # Pastrami costs $2 more than a Reuben, so its cost is x + $2
    pastrami_cost = x + 2

    # He sells 10 Reubens and 5 Pastrami sandwiches and earns $55
    total_sales = (10 * x) + (5 * pastrami_cost)
    if total_sales == 55:
        result = pastrami_cost
    else:
        result = "No solution found"
    return result

print(solution())