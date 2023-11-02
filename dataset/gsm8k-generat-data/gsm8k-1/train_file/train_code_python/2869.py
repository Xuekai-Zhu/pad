def solution():
    """Hanna has $300. She wants to buy roses at $2 each and give some of the roses to her friends, Jenna and Imma. Jenna will receive 1/3 of the roses, and Imma will receive 1/2 of the roses. How many roses does Hanna give to her friends?"""
    budget = 300
    cost_per_rose = 2
    total_roses = budget // cost_per_rose
    jenna_roses = total_roses // 3
    imma_roses = total_roses // 2
    hanna_gives = jenna_roses + imma_roses
    result = hanna_gives
    return result

print(solution())