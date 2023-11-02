def solution():
    total_spent = 300
    shoes_spent = 2 * shirt_spent + 9
    shirt_spent = (total_spent - shoes_spent) / 3
    result = shirt_spent
    return result

print(solution())