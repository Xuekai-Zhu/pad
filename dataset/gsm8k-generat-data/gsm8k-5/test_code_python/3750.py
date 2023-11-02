def solution():
    dolls = 12000  # The factory made 12000 dolls and their accessories
    shoes = dolls * 2  # Each doll has 2 shoes
    bags = dolls * 3  # Each doll has 3 bags
    cosmetics = dolls  # Each doll has 1 set of cosmetics
    hats = dolls * 5  # Each doll has 5 hats

    # Calculate the machine operation time for dolls and accessories
    doll_time = dolls * 45  # Each doll takes 45 seconds to make
    shoes_time = shoes * 10  # Each pair of shoes takes 10 seconds to make
    bags_time = bags * 10  # Each bag takes 10 seconds to make
    cosmetics_time = cosmetics * 10  # Each set of cosmetics takes 10 seconds to make
    hats_time = hats * 10  # Each hat takes 10 seconds to make

    # Calculate the total combined machine operation time
    total_time = doll_time + shoes_time + bags_time + cosmetics_time + hats_time
    result = total_time
    return result

print(solution())