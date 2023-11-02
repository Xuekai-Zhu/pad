def solution():
    total_utensils = 108
    num_pencils = 5
    num_pencils += 1
    num_pens = (total_utensils - (num_pencils * 2)) / 2
    result = num_pens
    return result

print(solution())