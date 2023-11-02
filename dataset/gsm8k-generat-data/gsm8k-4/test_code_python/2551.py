def solution():
    """Going into the final game, Duke is so close to breaking the school's record for most points scored in a basketball season.
    He only needs 17 more points to tie the record. By the end of the game, Duke breaks the record by 5 points.
    The old record was 257 points.
    In the final game, Duke made 5 free throws (worth one point), and 4 regular baskets (worth two points), and some three-pointers.
    Normally, he scores 2 three-pointers a game.
    How many more three-pointers did he score in the final game compared to his normal amount?"""
    # Define the points for each type of shot
    FREE_THROW_POINTS = 1
    REGULAR_BASKET_POINTS = 2
    THREE_POINTER_POINTS = 3

    # Define the old record and the points Duke needs to tie and break the record
    old_record = 257
    points_to_tie = 17
    points_to_break = points_to_tie + 5

    # Calculate Duke's points before the final game
    initial_points = old_record + points_to_tie

    # Calculate Duke's points from the final game
    final_points = ((5 * FREE_THROW_POINTS) +
                    (4 * REGULAR_BASKET_POINTS) +
                    (x * THREE_POINTER_POINTS))

    # Calculate the number of extra three-pointers Duke made compared to his normal amount
    extra_three_pointers = (final_points - initial_points) // THREE_POINTER_POINTS - 2

    # Return the result
    result = extra_three_pointers
    return result

print(solution())