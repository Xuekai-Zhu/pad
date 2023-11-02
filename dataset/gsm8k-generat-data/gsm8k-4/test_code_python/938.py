def solution():
    """Joe plays a soccer tournament with his team. Matches won score 3 points for the winning team and tied matches score 1 point for both teams. Joe and his team won 1 game and drew 3. The first-place team has won 2 games and tied 2. By how many points did the first-place team beat Joe's team?"""
    # Define the number of games won and tied by Joe's team
    joe_wins = 1
    joe_ties = 3

    # Calculate the total points earned by Joe's team
    joe_points = joe_wins * 3 + joe_ties * 1

    # Define the number of games won and tied by the first-place team
    first_wins = 2
    first_ties = 2

    # Calculate the total points earned by the first-place team
    first_points = first_wins * 3 + first_ties * 1

    # Calculate the difference in points between the two teams
    difference = first_points - joe_points

    result = difference
    return result

print(solution())