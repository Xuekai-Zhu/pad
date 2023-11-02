def solution():
    # Cost of the sandwiches
    sandwich_cost = 2 * 7.75

    # Cost of the salami
    salami_cost = 4.00

    # Cost of the brie (3 times the cost of salami)
    brie_cost = 3 * salami_cost

    # Cost of the olives (1/4 pound at $10 per pound)
    olives_cost = (1/4) * 10.00

    # Cost of the feta cheese (1/2 pound at $8 per pound)
    feta_cost = (1/2) * 8.00

    # Cost of the additional french bread
    bread_cost = 2.00

    # Total cost
    total_cost = sandwich_cost + salami_cost + brie_cost + olives_cost + feta_cost + bread_cost
    result = total_cost
    return result

print(solution())