def solution():
    # Calculate the total number of points Duke needed to tie the record
    points_needed = 17

    # Add the record and points needed to tie it to get the target score
    target_score = 257 + points_needed

    # Subtract the 5 free throws and 4 regular baskets to get the number of points Duke scored from 3-pointers
    points_from_threes = target_score - 5 - (4 * 2)

    # Calculate Duke's normal number of points from 3-pointers in a game
    normal_threes = 2

    # Calculate the difference between the number of 3-pointers Duke made in the final game and his normal amount
    diff = (points_from_threes / 3) - normal_threes

    result = diff
    return result

print(solution())