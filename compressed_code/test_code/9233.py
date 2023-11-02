def solution():
    
    total_candy = 63
    bags = 9
    chocolate_bags = 2 + 3
    non_chocolate_bags = bags - chocolate_bags
    non_chocolate_candy = (total_candy // bags) * non_chocolate_bags
    result = non_chocolate_candy
    return result

print(solution())