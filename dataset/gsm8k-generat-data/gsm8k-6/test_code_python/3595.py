def solution():
    mangoes = 400  # kg of mangoes produced
    apples = 2 * mangoes  # kg of apples produced
    oranges = mangoes + 200  # kg of oranges produced
    total_produce = mangoes + apples + oranges  # total kg of fruits produced
    total_money = total_produce * 50  # total amount of money earned
    result = total_money
    return result

print(solution())