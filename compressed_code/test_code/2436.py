def solution():
    
    rose_bushes = 6
    rose_bush_price = 75
    aloes = 2
    aloe_price = 100
    total_spent = (rose_bushes * rose_bush_price) + (aloes * aloe_price)
    for_friend = 2 * rose_bush_price
    for_himself = total_spent - for_friend
    result = for_himself
    return result

print(solution())