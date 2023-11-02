def solution():
    # Calculate the number of marbles Katrina has
    katrina_marbles = 85 / 5  # Mabel has 5 times as many marbles as Katrina
    amanda_marbles = (2 * katrina_marbles) - 12  # Amanda needs 12 more marbles to have twice as many marbles as Katrina
    difference = 85 - amanda_marbles  # Calculate the difference between the number of marbles Mabel has and Amanda has
    result = difference
    return result

print(solution())