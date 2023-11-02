def solution():
    fish = 50  # There were 50 fish in the pond
    tadpoles = 3 * fish  # There were 3 times as many tadpoles as fish
    curtis_fish = 7  # Curtis caught 7 fish
    tadpoles -= tadpoles / 2  # Half the tadpoles developed into frogs

    # Calculate the difference between the number of tadpoles and fish in the pond
    difference = tadpoles - (fish - curtis_fish)
    result = difference
    return result

print(solution())