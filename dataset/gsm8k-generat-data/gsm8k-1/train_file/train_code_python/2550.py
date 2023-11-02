def solution():
    """Going into the final game, Duke is so close to breaking the school's record for most points scored in a basketball season. He only needs 17 more points to tie the record. By the end of the game, Duke breaks the record by 5 points. The old record was 257 points. In the final game Duke made 5 free throws (worth one point), and 4 regular baskets (worth two points), and some three-pointers. Normally, he scores 2 three-pointers a game. How many more three-pointers did he score in the final game compared to his normal amount?"""
    points_needed_to_tie_record = 17
    points_broken_by = 5
    old_record = 257
    free_throws = 5
    regular_baskets = 4
    normal_three_pointers = 2
    total_points_scored = old_record + points_needed_to_tie_record + points_broken_by
    points_scored_from_three_pointers = total_points_scored - (free_throws + regular_baskets) - old_record - points_needed_to_tie_record - points_broken_by
    extra_three_pointers = points_scored_from_three_pointers - normal_three_pointers
    result = extra_three_pointers
    return result

print(solution())