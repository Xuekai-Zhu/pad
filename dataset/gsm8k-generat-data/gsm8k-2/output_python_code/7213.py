def solution():
    """Phil started his day with $40. He bought a slice of pizza for $2.75, a soda for $1.50 and a pair of jeans for $11.50. If he has nothing but quarters left of his original money, how many quarters does he now have?"""
    starting_balance = 40
    pizza_cost = 2.75
    soda_cost = 1.5
    jeans_cost = 11.5
    total_spent = pizza_cost + soda_cost + jeans_cost
    remaining_balance = starting_balance - total_spent
    quarters = remaining_balance * 4 / 1
    result = quarters
    return result

print(solution())