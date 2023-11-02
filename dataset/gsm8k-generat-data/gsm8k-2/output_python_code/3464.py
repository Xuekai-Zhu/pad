def solution():
    """Wyatt's mother gave him $74 to go to the store. Wyatt bought 5 loaves of bread and 4 cartons of orange juice. Each loaf of bread cost $5 and each carton of orange juice cost $2. How much money does Wyatt have left?"""
    bread_cost = 5
    orange_juice_cost = 2
    bread_count = 5
    orange_juice_count = 4
    total_spent = (bread_cost * bread_count) + (orange_juice_cost * orange_juice_count)
    money_left = 74 - total_spent
    result = money_left
    return result

print(solution())