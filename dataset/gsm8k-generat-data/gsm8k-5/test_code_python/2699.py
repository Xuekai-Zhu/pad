def solution():
    # Number of students who played kickball on Wednesday
    wednesday_players = 37

    # Number of students who played kickball on Thursday
    thursday_players = wednesday_players - 9

    # Total number of students who played kickball on both days
    total_players = wednesday_players + thursday_players

    result = total_players
    return result

print(solution())