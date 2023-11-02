def solution():
    
    hanna_budget = 300
    rose_price = 2
    roses_bought = hanna_budget // rose_price
    jenna_roses = roses_bought // 3
    imma_roses = roses_bought // 2
    total_roses_given = jenna_roses + imma_roses
    result = total_roses_given
    return result

print(solution())