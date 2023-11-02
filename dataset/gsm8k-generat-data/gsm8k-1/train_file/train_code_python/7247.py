def solution():
    """Mikail's birthday is tomorrow. He will be 3 times older than he was when he was three. On his birthday, his parents give him $5 for every year old he is. How much money will they give him?"""
    age_on_birthday = 3 * 3
    money_per_year = 5
    money_received = age_on_birthday * money_per_year
    result = money_received
    return result

print(solution())