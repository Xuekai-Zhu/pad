def solution():
    """Andrea has 8 more apples than Jamal and half as many bananas as Jamal. Jamal has 4 more bananas than apples. How many fruits are there if Andrea has 52 apples?"""
    andrea_apples = 52
    Jamal_apples = andrea_apples - 8
    jamal_bananas = Jamal_apples + 4
    andrea_bananas = jamal_bananas / 2
    total_fruits = andrea_apples + Jamal_apples + andrea_bananas + jamal_bananas
    result = total_fruits
    return result

print(solution())