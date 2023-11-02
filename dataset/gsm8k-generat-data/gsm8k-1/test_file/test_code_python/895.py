def solution():
    """Susan made 100 cookies for Christmas and was going to equally divide them between her 6 nephews. Before Susan could package them, her husband snuck 4 cookies for himself. How many cookies will each of Susan’s nephews get?"""
    total_cookies = 100
    husband_cookies = 4
    nephew_cookies = (total_cookies - husband_cookies) / 6
    result = nephew_cookies
    return result

print(solution())