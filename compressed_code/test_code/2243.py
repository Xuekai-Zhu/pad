def solution():
    
    fish = 50
    tadpoles = 3 * fish
    curtis_fish = 7
    tadpoles_to_frogs = tadpoles / 2

    fish_left = fish - curtis_fish
    tadpoles_left = tadpoles - tadpoles_to_frogs

    difference = tadpoles_left - fish_left
    result = difference
    return result

print(solution())