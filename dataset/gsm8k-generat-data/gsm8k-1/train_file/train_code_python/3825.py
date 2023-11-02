def solution():
    """While shopping, Greg spent 300$ on a shirt and shoes. If Greg spent 9 more than twice as much on shoes as he did a shirt, how much did Greg spend on a shirt?"""
    total_spent = 300
    shoes_spent = 2 * shirt_spent + 9
    shirt_spent = (total_spent - shoes_spent) / 2
    result = shirt_spent
    return result

print(solution())