def solution():
    """Billy's mom sends him to get ketchup. She gives him $10 and tells him to get the best deal on ketchup that he can and to spend all $10 on ketchup. He finds a bottle with 10 oz that cost $1 each. He finds a bottle that costs $2 that contains 16 ounces. He finds a bottle with 25 ounces that costs $2.5. He finds a $5 bottle that contains 50 ounces. Finally, he finds a $10 bottle with 200 ounces. How many bottles of ketchup does he buy?"""
    money = 10
    options = [(10, 1), (16, 2), (25, 2.5), (50, 5), (200, 10)]
    remaining_money = money
    total_ounces = 0
    for option in options:
        while remaining_money >= option[1]:
            remaining_money -= option[1]
            total_ounces += option[0]
    result = total_ounces // 10
    return result

print(solution())