def solution():
    """On Wednesday, 37 students played kickball. On Thursday, 9 fewer students played kickball. How many students played kickball on Wednesday and Thursday?"""
    # Define the number of students who played kickball on Wednesday
    wednesday_players = 37

    # Define the number of students who played kickball on Thursday
    thursday_players = wednesday_players - 9

    # Calculate the total number of students who played kickball on both days
    total_players = wednesday_players + thursday_players

    # return the result
    result = total_players
    return result

print(solution())