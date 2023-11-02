def solution():
    total_marbles = 85  # Josh has a total of 85 marbles
    red_marbles = 14  # There are 14 red marbles
    blue_marbles = 3 * red_marbles  # There are 3 times as many blue marbles as red
    yellow_marbles = total_marbles - red_marbles - blue_marbles  # The rest of the marbles are yellow

    result = yellow_marbles
    return result

print(solution())