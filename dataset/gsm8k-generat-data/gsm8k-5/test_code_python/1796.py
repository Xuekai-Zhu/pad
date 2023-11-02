def solution():
    total_rocks = 10  # Dennis collected 10 rocks
    rocks_after_fish = total_rocks / 2  # The fish ate half of the rocks
    rocks_after_spit = rocks_after_fish + 2  # Dennis was able to make the fish spit two rocks out

    result = rocks_after_spit
    return result

print(solution())