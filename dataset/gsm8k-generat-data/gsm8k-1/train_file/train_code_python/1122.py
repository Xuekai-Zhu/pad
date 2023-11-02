def solution():
    """David found $12 on the street. He then gave it to his friend Evan who has $1 and needed to buy a watch worth $20. How much does Evan still need?"""
    found_money = 12
    evan_money = 1
    watch_cost = 20
    total_money = found_money + evan_money
    amount_left = watch_cost - total_money
    result = amount_left
    return result

print(solution())