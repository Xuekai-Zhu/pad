def solution():
    # Define the number of students who played kickball on Wednesday
    wednesday_players = 37

    # Calculate the number of students who played kickball on Thursday
    thursday_players = wednesday_players - 9

    # Calculate the total number of students who played kickball on both days
    total_players = wednesday_players + thursday_players
    result = total_players
    return result

print(solution())