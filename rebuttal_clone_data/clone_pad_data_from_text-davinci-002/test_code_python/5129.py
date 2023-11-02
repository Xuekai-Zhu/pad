def solution():
    grapes = 100
    strawberries = grapes * (3/5)
    fruits_given_away = (grapes + strawberries) * (1/5)
    total_fruits = grapes + strawberries - fruits_given_away
    result = total_fruits
    return result

print(solution())