def solution():
    """Elsa's hockey team just made the playoffs along with two other teams. They make the playoffs by having the top three highest points for their records. Teams get 2 points for a win, 1 point for a tie, and zero points for a loss. The first-place team has 12 wins and 4 ties. The second-place team has 13 wins and 1 tie. Elsa's team has 8 wins and 10 ties. What is the average number of points for the playoff teams?"""
    first_place_points = 12 * 2 + 4 * 1
    second_place_points = 13 * 2 + 1 * 1
    elsa_points = 8 * 2 + 10 * 1
    playoff_points = first_place_points + second_place_points + elsa_points
    avg_points = playoff_points / 3
    result = avg_points
    return result

print(solution())