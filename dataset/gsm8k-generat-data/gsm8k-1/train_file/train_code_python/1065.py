def solution():
    """George and Amelia are picking oranges and apples at an orchard. George picks 45 oranges and 5 more apples than Amelia. Amelia picks 18 fewer oranges than George and 15 apples. How many fruits do they pick altogether?"""
    george_oranges = 45
    amelia_oranges = george_oranges - 18
    amelia_apples = 15
    george_apples = amelia_apples + 5
    total_fruits = george_oranges + amelia_oranges + george_apples + amelia_apples
    result = total_fruits
    return result

print(solution())