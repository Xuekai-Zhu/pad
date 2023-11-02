def solution():
    jackets_purchased = 4
    t_shirts_purchased = 9
    jackets_free = jackets_purchased // 2
    t_shirts_free = t_shirts_purchased // 3
    total_clothes = jackets_purchased + t_shirts_purchased + jackets_free + t_shirts_free
    result = total_clothes
    
    return result

print(solution())