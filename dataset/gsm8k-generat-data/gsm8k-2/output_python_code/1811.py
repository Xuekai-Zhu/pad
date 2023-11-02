def solution():
    """Bret takes a 9 hour train ride to go to Boston. He spends 2 hours reading a book, 1 hour to eat his dinner, and 3 hours watching movies on his computer. How many hours does he have left to take a nap?"""
    total_hours = 9
    hours_spent = 2 + 1 + 3
    nap_hours = total_hours - hours_spent
    result = nap_hours
    return result

print(solution())