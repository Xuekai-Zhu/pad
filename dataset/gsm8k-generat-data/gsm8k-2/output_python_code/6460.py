def solution():
    """John had $200. He gave 3/8 of his money to his mother and 3/10 to his father. How much money did John have left?"""
    john_money = 200
    mother_money = john_money * (3/8)
    father_money = john_money * (3/10)
    total_money_given_away = mother_money + father_money
    money_left = john_money - total_money_given_away
    result = money_left
    return result

print(solution())