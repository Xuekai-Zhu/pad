def solution():
    """Janet goes to the mall and spends $3.50 on ice cream, $7.50 each for movie tickets for herself and her younger sister, and $8.50 on a bracelet. If her parents gave her $40, how many dollars does she have left?"""
    total_spent = 3.5 + 2 * 7.5 + 8.5
    initial_money = 40
    money_left = initial_money - total_spent
    result = money_left
    return result

print(solution())