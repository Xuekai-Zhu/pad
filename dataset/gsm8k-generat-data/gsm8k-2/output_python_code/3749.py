def solution():
    """Last month, a factory made 12000 dolls and their associated accessories. The accessories for each doll included 2 shoes, 3 bags, 1 set of cosmetics, and 5 hats. If each doll took 45 seconds to make and each accessory took 10 seconds to make, what was the total combined machine operation time, in seconds, required to manufacture all of the dolls and their accessories?"""
    dolls = 12000
    shoes = dolls * 2
    bags = dolls * 3
    cosmetics = dolls * 1
    hats = dolls * 5

    total_time = (dolls * 45) + (shoes * 10) + (bags * 10) + (cosmetics * 10) + (hats * 10)

    result = total_time
    return result

print(solution())