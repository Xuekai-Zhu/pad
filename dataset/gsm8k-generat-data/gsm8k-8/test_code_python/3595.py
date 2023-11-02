def solution():
    # Define the total produce of mangoes and calculate the total produce of apples and oranges
    mangoes = 400
    apples = 2 * mangoes
    oranges = mangoes + 200

    # Calculate the total amount of produce and the total amount of money earned from selling the mangoes
    total_produce = mangoes + apples + oranges
    money_earned = mangoes * 50

    result = money_earned
    return result

print(solution())