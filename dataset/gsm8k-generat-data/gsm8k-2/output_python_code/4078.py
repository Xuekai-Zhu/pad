def solution():
    """Clare's mother gave her $47 to go to the store. Clare bought 4 loaves of bread and 2 cartons of milk. Each loaf of bread cost $2 and each carton of milk cost $2. How much money does Clare have left?"""
    total_cost = (4 * 2) + (2 * 2)
    remaining_money = 47 - total_cost
    result = remaining_money
    return result

print(solution())