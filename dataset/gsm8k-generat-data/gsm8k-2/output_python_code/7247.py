def solution():
    """Mikail's birthday is tomorrow. He will be 3 times older than he was when he was three. On his birthday, his parents give him $5 for every year old he is. How much money will they give him?"""
    current_age = 3 * 3
    money_per_year = 5
    total_money = current_age * money_per_year
    result = total_money
    return result

print(solution())