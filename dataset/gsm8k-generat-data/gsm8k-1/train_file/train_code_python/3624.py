def solution():
    """At Ken's local store, a pound of steak is going for $7. He decides to get two pounds. At the till, he pays using a $20 bill. How much money will he get back?"""
    cost_per_pound = 7
    pounds = 2
    total_cost = cost_per_pound * pounds
    payment = 20
    change = payment - total_cost
    result = change
    return result

print(solution())