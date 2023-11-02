def solution():
    """Marly is making soup. He adds 2 quarts of milk and three times as much chicken stock to 1 quart of pureed vegetables. Then he divides the soup into bags that can hold 3 quarts each. How many bags does he need?"""
    milk = 2
    vegetables = 1
    chicken_stock = 3 * vegetables
    soup = milk + vegetables + chicken_stock
    bags_needed = soup // 3
    if soup % 3 != 0:
        bags_needed += 1
    result = bags_needed
    return result

print(solution())