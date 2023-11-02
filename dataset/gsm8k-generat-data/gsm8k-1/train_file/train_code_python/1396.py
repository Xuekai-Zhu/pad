def solution():
    """Marly is making soup. He adds 2 quarts of milk and three times as much chicken stock to 1 quart of pureed vegetables. Then he divides the soup into bags that can hold 3 quarts each. How many bags does he need?"""
    milk = 2
    veg = 1
    stock = 3 * veg
    soup = milk + veg + stock
    bags_needed = soup // 3 + (soup % 3 > 0)
    result = bags_needed
    return result

print(solution())