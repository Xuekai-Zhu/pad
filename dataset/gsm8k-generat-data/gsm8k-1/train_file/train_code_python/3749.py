def solution():
    """Last month, a factory made 12000 dolls and their associated accessories. The accessories for each doll included 2 shoes, 3 bags, 1 set of cosmetics, and 5 hats. If each doll took 45 seconds to make and each accessory took 10 seconds to make, what was the total combined machine operation time, in seconds, required to manufacture all of the dolls and their accessories?"""
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