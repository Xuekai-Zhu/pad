def solution():
    num_given_todd = 4
    num_given_alisha = num_given_todd * 2
    num_given_bobby = 4 * num_given_alisha - 5
    total_given = num_given_todd + num_given_alisha + num_given_bobby

    total = total_given + 6
    result = total
    return result

print(solution())