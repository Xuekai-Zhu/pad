def solution():
    """Hanna has $300. She wants to buy roses at $2 each and give some of the roses to her friends, Jenna and Imma.
    Jenna will receive 1/3 of the roses, and Imma will receive 1/2 of the roses. How many roses does Hanna give to her friends?"""
    hanna_budget = 300
    rose_price = 2
    roses_bought = hanna_budget // rose_price
    jenna_roses = roses_bought // 3
    imma_roses = roses_bought // 2
    total_roses_given = jenna_roses + imma_roses
    result = total_roses_given
    return result

print(solution())