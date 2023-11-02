def solution():
    # Define the number of people who watched the second game
    second_game = 80

    # Calculate the number of people who watched the first game
    first_game = second_game - 20

    # Calculate the number of people who watched the third game
    third_game = second_game + 15

    # Calculate the total number of people who watched the games this week
    total_this_week = first_game + second_game + third_game

    # Calculate the difference between the total number of people who watched this week and last week
    difference = total_this_week - 200
    result = difference
    return result

print(solution())