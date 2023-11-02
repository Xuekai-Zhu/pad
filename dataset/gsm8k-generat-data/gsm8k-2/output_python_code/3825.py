def solution():
    """While shopping, Greg spent 300$ on a shirt and shoes. If Greg spent 9 more than twice as much on shoes as he did a shirt, how much did Greg spend on a shirt?"""
    total_spent = 300
    shoe_cost = 2 * shirt_cost + 9
    shirt_cost = (total_spent - shoe_cost) / 2
    result = shirt_cost
    return result

print(solution())