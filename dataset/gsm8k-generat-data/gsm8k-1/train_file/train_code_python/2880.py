def solution():
    """There were 50 fish in a pond and 3 times as many tadpoles. If Curtis catches 7 fish and half the tadpoles develop into frogs, how many more tadpoles than fish are there in the pond now?"""
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