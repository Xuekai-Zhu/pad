def solution():
    """David found $12 on the street. He then gave it to his friend Evan who has $1 and needed to buy a watch worth $20. How much does Evan still need?"""
    david_found = 12
    evan_has = 1
    watch_price = 20
    total_money = david_found + evan_has
    still_needed = watch_price - total_money
    result = still_needed
    return result

print(solution())