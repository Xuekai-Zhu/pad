def solution():
    """Going into the final game, Duke is so close to breaking the school's record for most points scored in a basketball season. He only needs 17 more points to tie the record. By the end of the game, Duke breaks the record by 5 points. The old record was 257 points. In the final game Duke made 5 free throws (worth one point), and 4 regular baskets (worth two points), and some three-pointers. Normally, he scores 2 three-pointers a game. How many more three-pointers did he score in the final game compared to his normal amount?"""
    normal_three_pointers = 2
    record_points = 257
    points_needed_to_tie = 17
    final_game_free_throws = 5
    final_game_baskets = 4 * 2
    final_game_points = record_points + 5
    points_scored_before_final_game = final_game_points - points_needed_to_tie - final_game_baskets - final_game_free_throws
    final_game_three_pointers = (final_game_points - points_scored_before_final_game) // 3 - normal_three_pointers
    result = final_game_three_pointers
    return result

print(solution())