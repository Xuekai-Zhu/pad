def solution():
    total_points = 345
    num_games = 15
    free_throws_per_game = 4
    two_pointers_per_game = 5

    # Calculate the total number of points scored from free throws
    free_throw_points = free_throws_per_game * num_games

    # Calculate the total number of points scored from two-point baskets
    two_pointer_points = two_pointers_per_game * num_games * 2

    # Calculate the total number of points scored from three-point baskets
    three_pointer_points = total_points - free_throw_points - two_pointer_points

    # Calculate the average number of three-point baskets per game
    avg_three_pointers = three_pointer_points / (num_games * 3)
    result = avg_three_pointers
    return result

print(solution())