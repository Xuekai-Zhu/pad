def solution():
    k_marbles = 85 / 5  # Katrina has 1/5 of Mabel's marbles
    a_marbles = (2 * k_marbles) - 12  # Amanda needs 12 more marbles to have twice as many as Katrina
    mabel_extra_marbles = 85 - a_marbles - k_marbles  # Mabel has this many more marbles than Amanda
    result = mabel_extra_marbles
    return result

print(solution())