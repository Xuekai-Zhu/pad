def solution():
    # Calculate the number of baby tarantulas in 5 egg sacs
    baby_tarantulas = 1000 * 5  # each egg sac contains 1000 tarantulas, and we have 5 egg sacs
    baby_tarantula_legs = baby_tarantulas * 8  # each tarantula has 8 legs
    # Calculate the number of baby tarantula legs in one less than 5 egg sacs
    less_egg_sacs = 4  # one less than 5 egg sacs
    less_baby_tarantulas = 1000 * less_egg_sacs  # each egg sac contains 1000 tarantulas, and we have one less egg sac
    less_baby_tarantula_legs = less_baby_tarantulas * 8  # each tarantula has 8 legs

    result = less_baby_tarantula_legs
    return result

print(solution())