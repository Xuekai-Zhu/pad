def solution():
    # Calculate the total points scored by Roosevelt High School in the tournament
    first_game = 30
    second_game = first_game / 2
    third_game = second_game * 3
    total_points = first_game + second_game + third_game + 50

    # Calculate the points scored by Greendale High School
    greendale_points = total_points - 10
    result = greendale_points
    return result

print(solution())