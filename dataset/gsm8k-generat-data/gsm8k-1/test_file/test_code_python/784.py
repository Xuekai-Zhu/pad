def solution():
    """John is raising money for a school trip. He has applied for help from the school, which has decided to cover half the cost of the trip. How much money is John missing if he has $50 and the trip costs $300?"""
    john_money = 50
    trip_cost = 300
    school_coverage = 0.5
    money_missing = (trip_cost * (1 - school_coverage)) - john_money
    result = money_missing
    return result

print(solution())