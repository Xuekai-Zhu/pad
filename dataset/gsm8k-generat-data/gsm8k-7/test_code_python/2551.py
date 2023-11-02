def solution():
    points_needed_to_tie = 17
    points_scored_in_final_game = 5
    old_record = 257
    free_throws_made = 5
    regular_baskets_made = 4
    normal_three_pointers = 2

    # Calculate the total points Duke scored in the final game
    total_points_scored = points_needed_to_tie + points_scored_in_final_game

    # Calculate the total points Duke scored in the final game from three-pointers
    final_game_three_pointers = total_points_scored - (free_throws_made + regular_baskets_made*2)

    # Calculate the total number of three-pointers Duke usually scores in a game
    normal_total_three_pointers = normal_three_pointers * 1  # assuming each three-pointer is worth 1 point

    # Calculate the difference between the number of three-pointers he made in the final game and what he usually makes
    extra_three_pointers_scored = final_game_three_pointers - normal_total_three_pointers
    result = extra_three_pointers_scored
    return result

print(solution())