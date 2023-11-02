def solution():
    # Calculate the number of rocks left after the fish ate half of them and spit two out
    initial_rocks = 10  # Dennis collected 10 rocks initially
    eaten_rocks = initial_rocks / 2  # Half of the rocks were eaten by the fish
    remaining_rocks = eaten_rocks - 2  # The fish spit out two rocks
    result = remaining_rocks
    return result

print(solution())