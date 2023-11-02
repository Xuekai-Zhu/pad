def solution():
    """Going into the final game, Duke is so close to breaking the school's record for most points scored in a basketball season. He only needs 17 more points to tie the record. By the end of the game, Duke breaks the record by 5 points. The old record was 257 points. In the final game Duke made 5 free throws (worth one point), and 4 regular baskets (worth two points), and some three-pointers. Normally, he scores 2 three-pointers a game. How many more three-pointers did he score in the final game compared to his normal amount?"""
    # Define important values
    RECORD = 257
    POINTS_NEEDED_TO_TIE = 17
    POINTS_BEYOND_RECORD = 5
    FREE_THROWS = 5
    REGULAR_BASKETS = 4
    NORMAL_THREE_POINTERS = 2

    # Calculate Duke's total points before the final game
    total_points_before = RECORD + POINTS_NEEDED_TO_TIE

    # Calculate Duke's total points in the final game
    total_points_final = total_points_before + POINTS_BEYOND_RECORD

    # Calculate the points Duke earned from free throws and regular baskets
    points_from_free_throws = FREE_THROWS
    points_from_regular_baskets = REGULAR_BASKETS * 2
    total_points_from_free_throws_and_regular_baskets = points_from_free_throws + points_from_regular_baskets

    # Calculate the points Duke earned from three-pointers
    points_from_normal_threes = NORMAL_THREE_POINTERS * (len(range(total_points_before, total_points_final, 3)) - 1)
    points_from_extra_threes = total_points_final - total_points_before - points_from_normal_threes
    total_points_from_threes = points_from_normal_threes + points_from_extra_threes

    # Calculate the difference in the number of three-pointers Duke made in the final game compared to his normal amount
    additional_threes = points_from_extra_threes // 3

    # Display the result
    result = additional_threes
    return result

print(solution())