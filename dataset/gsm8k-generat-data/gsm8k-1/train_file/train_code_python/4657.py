def solution():
    """Toby’s father gave him $343 for passing the test. Toby decided to share it with his two brothers, so he gave each of them 1/7 of $343. How many dollars are left for Toby?"""
    total_money = 343
    money_per_brother = (1/7) * total_money
    money_left = total_money - (2 * money_per_brother)
    result = money_left
    return result

print(solution())