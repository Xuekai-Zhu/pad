def solution():
    """Jeff plays tennis for 2 hours. He scores a point every 5 minutes. He wins a match when he scores 8 points. How many games did he win?"""
    # Calculate the total number of points Jeff scored in 2 hours
    points = (2 * 60) // 5

    # Calculate the number of games Jeff won
    games = points // 8

    # Display the number of games won
    result = games
    return result

print(solution())