def solution():
    """Jada, Rory, and Kora make clay dishes to present as art for their school project. Jada makes twice as many clay dishes as Rory, while Rory makes 20 more clay dishes than Kora. If Kora made 20 dishes, how many clay dishes they all make together?"""
    kora_dishes = 20
    rory_dishes = kora_dishes + 20
    jada_dishes = rory_dishes * 2
    total_dishes = kora_dishes + rory_dishes + jada_dishes
    result = total_dishes
    return result

print(solution())