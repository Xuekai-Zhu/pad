def solution():
    """Mikail's birthday is tomorrow. He will be 3 times older than he was when he was three. On his birthday, his parents give him $5 for every year old he is. How much money will they give him?"""
    # Calculate Mikail's current age
    current_age = 3 * (1 + 3)

    # Calculate the amount of money Mikail will receive
    money = current_age * 5

    # return the result
    result = money
    return result

print(solution())