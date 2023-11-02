def solution():
    """Blake goes to the grocery store and spends $40 on oranges, $50 on apples, and $60 on mangoes. If he has $300, how much change was he given?"""
    total_spent = 40 + 50 + 60
    money_given = 300
    change = money_given - total_spent
    result = change
    return result

print(solution())