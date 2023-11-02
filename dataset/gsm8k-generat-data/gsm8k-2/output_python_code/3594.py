def solution():
    """Mr. Sergio is a fruit grower producing apples, mangoes and oranges. In a particular season, the total produce of apples was twice the total produce of mangoes, and the total produce of oranges was 200 kg more than that of mangoes. If his farm produced 400 kg of mangoes and he sold the fruits at $50 per kg, calculate the total amount of money he got in that season."""
    mangoes = 400
    apples = 2 * mangoes
    oranges = mangoes + 200
    total_produce = mangoes + apples + oranges
    fruit_price = 50
    total_money = total_produce * fruit_price
    result = total_money
    return result

print(solution())