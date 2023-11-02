def solution():
    """Debora has 12 more dresses than Melissa. Melissa has half the number of dresses Emily has. If Emily has 16 dresses, how many dresses do the three of them have in total?"""
    emily_dresses = 16
    melissa_dresses = emily_dresses / 2
    debora_dresses = melissa_dresses + 12
    total_dresses = emily_dresses + melissa_dresses + debora_dresses
    result = total_dresses
    return result

print(solution())