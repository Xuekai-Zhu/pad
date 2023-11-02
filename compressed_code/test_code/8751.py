def solution():
    
    dolls = 12000
    shoes_per_doll = 2
    bags_per_doll = 3
    cosmetics_per_doll = 1
    hats_per_doll = 5
    total_accessories_per_doll = shoes_per_doll + bags_per_doll + cosmetics_per_doll + hats_per_doll
    time_per_doll = 45 + (total_accessories_per_doll * 10)
    total_time = dolls * time_per_doll
    result = total_time
    return result

print(solution())