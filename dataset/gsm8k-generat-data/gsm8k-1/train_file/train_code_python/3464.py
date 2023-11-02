def solution():
    """Wyatt's mother gave him $74 to go to the store. Wyatt bought 5 loaves of bread and 4 cartons of orange juice. Each loaf of bread cost $5 and each carton of orange juice cost $2. How much money does Wyatt have left?"""
    total_spent = (5*5) + (4*2)
    money_left = 74 - total_spent
    result = money_left
    return result

print(solution())