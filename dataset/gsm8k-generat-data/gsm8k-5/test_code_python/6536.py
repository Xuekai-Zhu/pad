def solution():
    # Number of people who watched the second game
    second_game = 80
    # Number of people who watched the first game
    first_game = second_game - 20
    # Number of people who watched the third game
    third_game = second_game + 15

    # Total number of people who watched the three games this week
    total_week = first_game + second_game + third_game

    # Total number of people who watched the games last week
    total_last_week = 200

    # Calculate the difference between the total number of people who watched the games this week and last week
    difference = total_week - total_last_week

    result = difference
    return result

print(solution())