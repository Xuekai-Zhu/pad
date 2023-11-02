def solution():
    
    pants_price = 0
    shirt_price = 0
    for i in range(1, 63):
        for j in range(1, 63):
            if (2*i + 5*j == 62) and (2*j == 20):
                pants_price = i
                shirt_price = j
    result = pants_price
    return result

print(solution())