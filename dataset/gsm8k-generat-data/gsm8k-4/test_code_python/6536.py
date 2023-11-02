def solution():
    """In three baseball games this week, eighty people watched the second game while 20 fewer people watched the first game than the second game. Then 15 more people watched the third than the second game. If there were a total of 200 people who watched the games last week, how many more people watched the games this week than last week?"""
    # Define the number of people who watched the second game
    second_game = 80

    # Calculate the number of people who watched the first game
    first_game = second_game - 20

    # Calculate the number of people who watched the third game
    third_game = second_game + 15

    # Calculate the total number of people who watched the games this week
    total_this_week = first_game + second_game + third_game

    # Calculate the difference between the total number of people who watched the games this week and last week
    difference = total_this_week - 200

    result = difference
    return result

print(solution())