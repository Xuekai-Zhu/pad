def solution():
    """Three friends: Mike, Jim, and Tony decided to play a game. After 3 rounds Mike has 21 points, Jim 3 points less than Mike, and Tony 2 times more than Mike. In the fourth round, every player gets an extra point if they have over 20 points. How many points do all three players have in total after the extra points had been distributed?"""
    mike_points = 21
    jim_points = mike_points - 3
    tony_points = mike_points * 2
    if mike_points > 20:
        mike_points += 1
    if jim_points > 20:
        jim_points += 1
    if tony_points > 20:
        tony_points += 1
    total_points = mike_points + jim_points + tony_points
    result = total_points
    return result

print(solution())