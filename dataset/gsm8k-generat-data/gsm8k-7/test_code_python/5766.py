def solution():
    # Haylee's guppies
    num_haylee = 3 * 12

    # Jose's guppies
    num_jose = num_haylee / 2

    # Charliz's guppies
    num_charliz = num_jose / 3

    # Nicolai's guppies
    num_nicolai = num_charliz * 4

    # Total number of guppies
    num_total = num_haylee + num_jose + num_charliz + num_nicolai
    result = num_total
    return result

print(solution())