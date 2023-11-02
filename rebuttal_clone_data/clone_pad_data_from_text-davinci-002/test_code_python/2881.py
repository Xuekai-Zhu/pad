def solution():
    fish = 50
    tadpoles = 3 * fish
    fish_caught = 7
    tadpoles_to_frogs = tadpoles / 2
    tadpoles_left = tadpoles - tadpoles_to_frogs - fish_caught
    fish_left = fish - fish_caught
    difference = tadpoles_left - fish_left
    result = difference
    return result

print(solution())