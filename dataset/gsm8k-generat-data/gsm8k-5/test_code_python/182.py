def solution():
    # Lisa's spending
    shirt_cost = 40
    jeans_cost = shirt_cost / 2
    coat_cost = shirt_cost * 2
    lisa_spending = shirt_cost + jeans_cost + coat_cost

    # Carly's spending
    carly_shirt_cost = shirt_cost / 4
    carly_jeans_cost = jeans_cost * 3
    carly_coat_cost = coat_cost / 4
    carly_spending = carly_shirt_cost + carly_jeans_cost + carly_coat_cost

    # Total spending
    total_spending = lisa_spending + carly_spending
    result = total_spending
    return result

print(solution())