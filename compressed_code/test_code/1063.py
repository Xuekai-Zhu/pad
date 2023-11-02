def solution():
    
    breeding_rabbits_first = 10
    kittens_first = breeding_rabbits_first * 10
    adopted_first = kittens_first / 2
    returned_first = 5
    remaining_first = kittens_first / 2 - returned_first
    breeding_rabbits_second = 10
    kittens_second = 60
    adopted_second = 4
    remaining_second = kittens_second - adopted_second
    total_rabbits = breeding_rabbits_first + remaining_first + breeding_rabbits_second + remaining_second
    result = total_rabbits
    return result

print(solution())