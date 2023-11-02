def solution():
    """Mark has an egg farm. His farm supplies one store with 5 dozen eggs and another store with 30 eggs each day. How many eggs does he supply these two stores in a week?"""
    eggs_store1 = 5 * 12
    eggs_store2 = 30
    eggs_per_week = (eggs_store1 + eggs_store2) * 7
    result = eggs_per_week
    return result

print(solution())