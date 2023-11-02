def solution():
    
    total_candy = 63
    bags = 9
    chocolate_hearts_bags = 2
    chocolate_kisses_bags = 3
    chocolate_bags = chocolate_hearts_bags + chocolate_kisses_bags
    non_chocolate_bags = bags - chocolate_bags
    non_chocolate_candy = (total_candy / bags) * non_chocolate_bags
    result = non_chocolate_candy
    return result

print(solution())