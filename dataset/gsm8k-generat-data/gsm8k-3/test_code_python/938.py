def solution():
    """Joe plays a soccer tournament with his team. Matches won score 3 points for the winning team and tied matches score 1 point for both teams. Joe and his team won 1 game and drew 3. The first-place team has won 2 games and tied 2. By how many points did the first-place team beat Joe's team?"""
    # Calculate the points earned by Joe's team
    joe_points = 1 * 3 + 3 * 1

    # Calculate the points earned by the first-place team
    first_place_points = 2 * 3 + 2 * 1

    # Calculate the point difference between the two teams
    point_difference = first_place_points - joe_points

    # Display the point difference
    result = point_difference
    return result

print(solution())