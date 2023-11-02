def solution():
    """In three baseball games this week, eighty people watched the second game while 20 fewer people watched the first game than the second game. Then 15 more people watched the third than the second game. If there were a total of 200 people who watched the games last week, how many more people watched the games this week than last week?"""
    second_game = 80
    first_game = second_game - 20
    third_game = second_game + 15
    total_this_week = first_game + second_game + third_game
    total_last_week = 200
    difference = total_this_week - total_last_week
    result = difference
    return result

print(solution())