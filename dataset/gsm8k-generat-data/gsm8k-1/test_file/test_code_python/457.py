def solution():
    """Shondra has 7 fewer plants than Toni. Toni has 60% more plants than Frederick. If Frederick has 10 plants, how many plants does Shondra have?"""
    frederick_plants = 10
    toni_plants = frederick_plants * 1.6
    shondra_plants = toni_plants - 7
    result = shondra_plants
    return result

print(solution())