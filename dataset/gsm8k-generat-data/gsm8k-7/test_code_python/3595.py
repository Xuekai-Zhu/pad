def solution():
    mangoes_produced = 400
    apples_produced = 2 * mangoes_produced
    oranges_produced = mangoes_produced + 200

    total_produce = mangoes_produced + apples_produced + oranges_produced

    total_income = total_produce * 50
    result = total_income
    return result

print(solution())