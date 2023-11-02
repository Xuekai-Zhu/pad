def solution():
    """The total cost of Olivia’s groceries was $42. The bananas cost her $12, the bread cost her $9, and the milk cost her $7. The only other groceries she bought were apples. In dollars, how much money did the apples cost her?"""
    total_cost = 42
    bananas_cost = 12
    bread_cost = 9
    milk_cost = 7
    apples_cost = total_cost - bananas_cost - bread_cost - milk_cost
    result = apples_cost
    return result

print(solution())