def solution():
    mangoes = 400  # Total produce of mangoes is 400 kg
    apples = 2 * mangoes  # Total produce of apples is twice the produce of mangoes
    oranges = mangoes + 200  # Total produce of oranges is 200 kg more than that of mangoes
    total_kg = mangoes + apples + oranges  # Total produce of all fruits

    # Calculate the total amount of money Mr. Sergio got by selling the fruits
    total_money = total_kg * 50
    result = total_money
    return result

print(solution())