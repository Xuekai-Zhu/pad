def solution():
    
    fish = 50
    tadpoles = fish * 3
    caught_fish = 7
    remaining_fish = fish - caught_fish
    developing_tadpoles = tadpoles / 2
    remaining_tadpoles = tadpoles - developing_tadpoles
    difference = remaining_tadpoles - remaining_fish
    result = difference
    return result

print(solution())